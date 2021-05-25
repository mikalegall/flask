# Python

Tero Karvisen [opissa](https://terokarvinen.com/2021/python-web-service-from-idea-to-production/ "Python Web Service From Idea to Production") saadut etätehtävät MarkDownilla tallennettuna ([Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)):
<br>
Kun on tarvetta samanaikaisuuden hallinnalle rinnakkaisilla [säikeillä (thread)](https://wiki.aalto.fi/download/attachments/72895679/luento12.pdf) ei arkkitehtuurisissa valinnoissa välttämättä kannattane suosia siltä osin Pythonia. Pythonissa ei ole erikseen public / private / protected metodeja eikä myöskään ole mitään gettereitä ja settereitä vaan attribuuttia voi käyttää suoraan. Python on niin sanotusti tyypittämätön kieli vaikka seillä tyypit ovatkin tuettu (vaihtuvat lennosta).


DB: Pythonille [SQLAlchemy](https://en.wikipedia.org/wiki/SQLAlchemy) (ORM) <--> [PostgreSQL](https://terokarvinen.com/search/?q=postgre)
<br>
(jolla myös [web-sivun lomakkeet](https://terokarvinen.com/2020/flask-automatic-forms/)
<br>
from wtforms.ext.sqlalchemy.orm import model_form
<br>
from flask_wtf import FlaskForm)

BE: Python ([Object-oriented programming](https://fi.wikipedia.org/wiki/Olio-ohjelmointi)) 

    sudo apt update 

    sudo apt upgrade

    sudo apt install python3

#Valinnainen https://en.wikipedia.org/wiki/IPython (toimii Anacondan mukana tulevan Jupyter Notebookin tavoin "input" & "output")
<br>
#sudo apt install ipython3

<br>

FE: Pythonille Djangon "kilpailija" [Flask](https://en.wikipedia.org/wiki/Flask_(web_framework)) (sisältää [Jinja2 HTML-muottimoottorin](https://jinja2docs.readthedocs.io/en/stable/)) fronttiin

        sudo apt install python3-flask

<br>
Perusaloitusrunko

    #Kerrotaan mistä kirjastosta (kirjastojen nimet pienellä alkukirjaimella) tuodaan haluttu luokka hyödynnettäväksi (luokkien nimet isolla alkukirjaimella)
    from flask import Flask

    #Flask-luokan konstruktori ottaa parametrikseen main-metodin
    app = Flask(__name__)

    #Endpoint
    @app.route('/nettiosoite')

    #Funktiot määritellään avainsanalla def ja lohko aloitetaan kaksoispisteellä
    def controller():
        #Funktion sisältämän lohkon sisennys on syntaksissa pakollista
        return "Moikka moi!"

    #Jos tiedostoa ajetaan suoraan komentoriviltä (eikä ole esim. importattu ipython3:seen) 
    if __name__ == "__main__":
        #Käynnistä paikallinen kehityspalvelin
    	app.run(debug=True, port=8888)
    #Käynnistyttyään vastaanottaa kutsun endpointissa
    http://127.0.0.1:8888/nettiosoite


Pilvipalveluja: [Linode](https://www.linode.com/pricing/), [Digital Ocean](https://www.digitalocean.com/pricing), [Hetzner](https://www.hetzner.com/cloud) jne.

Deplpyment Pythonille [mod_wsgi](https://pypi.org/project/mod-wsgi/) <--> Apache2

Domain: [Namecheap](https://www.namecheap.com/domains/#pricing), [Gandi](https://shop.gandi.net/en/domain/suggest?options=1&search=halpa)


***

## Tehtävät

Pythonin perussyntaksi versiolla 1.0 on avattu juurta jaksaen suomenkielellä sijainnissa https://web.archive.org/web/20180517070419/http://www.cs.hut.fi/~ttsirkia/Python.pdf

Vaikka versio 2.0 on jo julkaistu kannattanee silti vielä jonkun aikaa toimia aiemmalla versiolla kunnes kaikki lastentaudit on sairastettu https://flask.palletsprojects.com/en/1.0.x/quickstart/


### [pw1.1 (Hei maailma)](https://terokarvinen.com/2021/python-web-service-from-idea-to-production/#pw1-hello-flask-world): HTML
https://github.com/mikalegall/flask/blob/main/hello_html/index.html
<br>
<br>
### [pw1.2 (Hei maailma) & pw1.4 (koodin kommentointi) ](https://terokarvinen.com/2021/python-web-service-from-idea-to-production/#pw1-hello-flask-world): Flask ja kommentointi
https://github.com/mikalegall/flask/blob/main/hello_flask/hello.py
<br>
<br>
### [pw1.3 (Hei maailma)](https://terokarvinen.com/2021/python-web-service-from-idea-to-production/#pw1-hello-flask-world): Python
https://github.com/mikalegall/flask/blob/main/hello_python/hello.py

<br>
<br>

### [pw2.1 (Tulosta käyttäjäsyöte sivulle)](https://terokarvinen.com/2021/python-web-service-from-idea-to-production/#pw2-muotit-ja-lomakkeet):
https://github.com/mikalegall/flask/tree/main/print_user_input
<br>
<br>
### [pw2.2 (Eri endpointit)](https://terokarvinen.com/2021/python-web-service-from-idea-to-production/#pw2-muotit-ja-lomakkeet):
https://github.com/mikalegall/flask/tree/main/tuplamuotti
<br>
<br>
### [pw2.3 (Silmukoi listan sisältö fronttiin)](https://terokarvinen.com/2021/python-web-service-from-idea-to-production/#pw2-muotit-ja-lomakkeet):
https://github.com/mikalegall/flask/tree/main/print_list_for_in
<br>
<br>
### [pw2.4 (Lomakerunko)](https://terokarvinen.com/2021/python-web-service-from-idea-to-production/#pw2-muotit-ja-lomakkeet):
https://github.com/mikalegall/flask/tree/main/form_minimum
