import urllib
import webapp2
import logging
import os

from google.appengine.ext import blobstore,db
from google.appengine.ext.blobstore import BlobInfo
from google.appengine.ext.webapp import blobstore_handlers 

# Template engine
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class FileRecord(db.Model):
  blob = blobstore.BlobReferenceProperty()
  
class MainHandler(webapp2.RequestHandler):
  def getRecordDate(handler, item):
    return item.blob.creation

  def get(self):

    # Order files by date desc
    files = sorted(FileRecord.all(), key=self.getRecordDate, reverse=True)

    template_values = {
      'files': files,
      'upload_url': blobstore.create_upload_url('/upload')
    }

    template = JINJA_ENVIRONMENT.get_template('pages/index.html')

    self.response.out.write(template.render(template_values))

class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
  def post(self):
    blob_info = self.get_uploads('file')[0]  # 'file' is file upload field in the form
    record = FileRecord(blob = blob_info)
    record.put()
    self.redirect('/')

class GetHandler(blobstore_handlers.BlobstoreDownloadHandler):
  def get(self, blob_key, filename):
    logging.info('GetHandler blob_key=%s filename=%s' % (blob_key, filename))
    blob_key = str(urllib.unquote(blob_key))
    record = FileRecord.get_by_id(int(blob_key))

    # Set content type and open file instead of download
    self.response.headers['Content-Type'] = record.blob.content_type

    # Add cache headers. Can cache forever because of unique ID in URL
    self.response.headers['Cache-Control'] = 'public'
    self.response.headers['Cache-Control: max-age'] = '31536000'
    self.response.headers['Expires'] = 'Thu, 31 Dec 2037 00:00:00 GMT'
    self.send_blob(record.blob,save_as=False)
    
class DeleteHandler(webapp2.RequestHandler):
  def get(self,blob_key):
    try:
      blob_key = urllib.unquote(blob_key)
      record = FileRecord.get_by_id(int(blob_key))
      
      record.blob.delete()
      record.delete()
    except:
      self.error(404)
    self.redirect('/')

app = webapp2.WSGIApplication([('/', MainHandler),
           ('/upload', UploadHandler),
           ('/delete/([^/]+)?', DeleteHandler),
           ('/([^/]+)?/([^/]+)?', GetHandler),

           # Obsolete route handler (retains backward compatibility)
           # See also app.yaml config "url: /get/(.*?)/(.*)"
           ('/get/([^/]+)?/([^/]+)?', GetHandler)], debug=True)