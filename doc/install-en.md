#Kaip Zubko!

If you woke up one morning here in Los Angeles and found Lithuanians with sharp teeth crawling up the beach with golf clubs to beat your brains out. What would you do?

If you found it's a problem for you, continue thinking, watch "Mad Max". Otherwise continue reading.

##How should I spell it?

Read it as "File sharing like Zubko" in English. Or "File sharing Zubko way". (Zubko is a surname; most probably with roots from Ukraine).

##WTF this crap is about?

It's a next generation of distributed file sharing.

Forget about torrents (and they smell like crime, right?). Now you have many smart gadgets and first of all you want to share file between them. Want to see a movie from your laptop on smart TV? Do you know how to set up a home wireless network considering your laptop runs Windows, you have iPhone in your pocket and you have a Linux based smart TV (like most of us)? We haven't learned it yet therefore "Kaip Zubko!" project began. Pardon, it's a lie, it actually began because we want to share files between a distributed team of people. But first learn how to share files across your devices and then you can easily switch to team sharing.

"Kaip Zubko!" wants to tell you that file sharing via cloud is easier. Even easier than setting up a home network. But make sure that you have a stable Internet plan so you'll get a fixed pay check at the end of the month.

To use "Kaip Zubko!" you'll need to set up a cloud web site. Then you'll install "Kaip Zubko!" application to it. Sounds difficult? We'll show that it's not. Or ask your 13 years old son to do it for you.

###STEP 0. Get a Google account
Get a gmail e-mail address. If you have one then skip this step.
Go to https://accounts.google.com and register your account. You'll need a mobile phone able to get SMS to enter it somewhere (no need for a smart phone).

###STEP 1. Set up your cloud application
Go to https://appengine.google.com and register. You'll need a mobile phone able to get SMS to enter it somewhere (no need for smart a phone; again).
Once you can login to https://appengine.google.com, create your application. You have to choose an unique application identifier. Of course, try mykaipzubko first, but if it's taken select another one. Say, mykaipzubko.appspot.com is a place you've got (replace mykaipzubko with your true app id further on).

###STEP 2. Download "Kaip Zubko!" code
Go to https://github.com/r-pankevicius/KaipZubko and download zip (icon in the right). If you run Windows, right click the file and unblock it.
Unzip it to C:\TEMP\KaipZubko folder.
Edit app.yaml file and change application in the first line from "kaipzubko" to your application ID on Google App Engine (mykaipzubko will be used further in the example as application ID).

###STEP 3. Install Python 2.7
Go to https://www.python.org/downloads/ and download Python 2.7.9 (not version 3!). Run installer and install it.

###STEP 4. Install Google AppEngine SDK for Python
Download the Google App Engine SDK for Python from https://cloud.google.com/appengine/downloads. Run installer and install it.

###STEP 5. Publish "Kaip Zubko!" code to mykaipzubko.appspot.com
Start Google App Engine Launcher, in menu select File, Add Existing Application, choose the folder C:\TEMP\KaipZubko and add it. Select your application in list. You should see somewhat like:

![Nice UI, isn't it?](https://github.com/r-pankevicius/KaipZubko/blob/master/doc/img/gae-launcher.png "Nice UI, isn't it?")

Press "Deploy" button and deploy it to mykaipzubko.appspot.com. The program will ask you to login with google account. Wait till it succeeds telling that "You can close this window now".

###STEP 6. Run "Kaip Zubko!" on mykaipzubko.appspot.com
Go to https://appengine.google.com/, select your application, open Versions tab and make uploaded version of your application the default one.

That's all. Now you have a "Kaip Zubko!" server running on http://mykaipzubko.appspot.com.

###Final words
Share with care!
