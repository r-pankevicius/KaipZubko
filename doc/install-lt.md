#Kaip Zubko!
Naujos kartos failų šarinimo sistema.

<i>"Šitie vaikinai sėja velnio sėklą."</i><br/>
Iš slaptos VSD pažymos Grybauskaitei ir Radijošou kronikų.<br/>

Tuoj įdiegsim: maždaug per 20-60 minučių ir pašarinsit ne blogiau už patį Zubko!

Tik rimtiems bachūriukams!

##Ką čia varai, bičiuks?

Jei turi Windowsinį laptopą, Samsungą kišenėj, tavo telikas yr Linūcha, tai kaip tu šarini vidiakus tarp jų? Kopijuoji į fliašiuką ir nešioji? Nu, tada daryk, kaip rašom ir pajusi skirtumą.

###0. Gauk Gmailą
Turbūt turi? Tai praleidžiam.

###1. Dabar eisim į debesis
Eik į https://appengine.google.com ir užsiregistruok. Gausi SMS ir įvesi, kur reikia. Reik tik biškiuką angliškai šarinti.
Kai galėsi įsiloginti į https://appengine.google.com, sukurk savo "aplikaciją". Reikės pasirinkti tokį vardą (application id), kad kiti lochai nežinotų. Pabandyk mykaipzubko iš pradžių, bet jei kitas bičiuks jį jau užėmė, sugalvok kitokį.

###2. Parsisiųsk slaptą "Kaip Zubko!" kodą
Eik į https://github.com/r-pankevicius/KaipZubko ir spaus "Download zip" (kažkur dešinėj). (Ir jei koks lochelis tau kada nors sakys, kad reikia žinoti, kas yra <code>git clone</code>, tai tu žinai, ką jam atsakyti. Tiesus-trumpas. Apie ką su juo daugiau šnekėti?)
Parsisiuntęs spausk dešinį pelės mygtuką ir "Unblock". Virusų mes nerašom, nemyžk į kelnes.
Išzipuok jį C:\TEMP\KaipZubko.
Atsidaryk app.yaml su kokiu notepadu ir pakeisk <code>application</code> pirmoj eilutėj iš "kaipzubko" (nu, mes ne lochai, tokį gerą vardą jau užėmėm) į tavo vardą (nu, į mykaipzubko, jei buvai greits).

###3. Įdiek Python 2.7
Eik į https://www.python.org/downloads/ ir parsisiųsk Python 2.7.9 (Bet ne 3-ią versiją! Ten toks olandas susigalvojo, kad jis anksčiau blogai rašė, o dabar geriau, bet pasaulis jo dar nesuprato).
Paspausk diegimo programkę (msi) ir įsidiek Pitoną.

###4. Įdiek Google AppEngine SDK Pitončikui
Iš https://cloud.google.com/appengine/downloads.

###5. Siųsk "Kaip Zubko!" kodą į debesis(į mykaipzubko.appspot.com)
Paleisk Google App Engine Launcher, iš meniu pasirink File, Add Existing Application, pasirink folderiuką C:\TEMP\KaipZubko ir pridėk.
Pasirink savo appsą sąraše. Turėtum matyt kažką tokio:

![Nu kaip?](https://github.com/r-pankevicius/KaipZubko/blob/master/doc/img/gae-launcher.png "Nu kaip?")

Spausk "Deploy" mygtuką ir siųsk visą kodą į mykaipzubko.appspot.com. Kai paprašys įsiloginti, taip ir padaryk. Palauk, kol pamatysi "You can close this window now". (Čia kažkas angliškai, kai brolis grįš iš Anglijos, paklausk, ką tai reiškia.)

###6. Paleisk "Kaip Zubko!" iš mykaipzubko.appspot.com
Eik į https://appengine.google.com/, pasirink savo programą (turbūt vienintelę, sunku nebus), spausk Versions ir aktyvuok ką tik nusiųstą versiją: mygtukas "Make Default".

Viskas. Dabar tu turi "Kaip Zubko!" serveriuką ant http://mykaipzubko.appspot.com. Siųsk ten savo failiukus ir duok draugeliams linkus.
