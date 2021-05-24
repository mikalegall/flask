from animal import *

#Luokka toteuttaa ylemmän luokan ottamalla sen parametrikseen
class Kissa(Animal):
        #Luokan metodissa on oltava parametrina self, joka viittaa olioon,
        #jossa metodia suoritetaan
        def sano_jotain(self):
	        return "Miaau"
