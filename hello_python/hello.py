from flask import Flask
from animal import *
from kissa import *

app = Flask(__name__)


#Main metodi suorittaa varsinaisen ohjelman
def main():
	eläin = Animal()
	print(eläin.sano_jotain())
	kisu = Kissa()
	print(kisu.sano_jotain())

#Jos tiedostoa ajetaan suoraan komentoriviltä (eikä ole esim. importattu ipython3:seen) 
if __name__ == "__main__":
	#Suorita main-metodi
	main()
