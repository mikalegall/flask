#Docstring
"Tästä kommentointi tavasta voi muodostaa dokumentaatiota" 

class Animal():
	#Docstring
	"Kuvaavaa ohjetekstiä voi kirjoittaa lainausmerkkien sisään"
	#Luokan attribuutti
	name = "Nimeämätön eläin"

	#Luokan metodissa on oltava parametrina self, joka viittaa olioon,
	#jossa metodia suoritetaan
	def sano_jotain(self):
	        return "Tunnistamaton (nimeämättömän eläimen) ääni"
