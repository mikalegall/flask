#Kerrotaan mistä kirjastosta (kirjastojen nimet pienellä alkukirjaimella) tuodaan haluttu luokka hyödynnettäväksi (luokkien nimet isolla alkukirjaimella)
from flask import Flask

#Flask-luokan konstruktori ottaa parametrikseen main-metodin
app = Flask(__name__)

#Käynnistä paikallinen kehityspalvelin
app.run()