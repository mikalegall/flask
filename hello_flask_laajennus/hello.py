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
    	#http://127.0.0.1:8888/nettiosoite
