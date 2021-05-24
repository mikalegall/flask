#Kirjastojen nimet pienellä ja luokkien nimet isolla
##Tuodaan flask-kirjastosta luokka nimeltä Flask
from flask import Flask

#Flask-luokan konstruktori ottaa parametrikseen main-metodin
app = Flask(__name__)

#Endpoint
@app.route("/")

#Funktiot määritellään avainsanalla def ja lohko aloitetaan kaksoispisteellä
def index():
    #Funktion sisältämän lohkon sisennys on pakollista
    return "Hei Mika!"
    

if __name__ == "__main__":
	app.run(debug=True, port=8888) #Paikallinen kehityspalvelin
