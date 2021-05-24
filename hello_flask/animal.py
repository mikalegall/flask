class Animal():
	#Luokan attribuutti
	name = "Generic animal"

	#Luokan metodissa on oltava parametrina self, joka viittaa olioon,
	#jossa metodia suoritetaan
	def sound(self):
        return "Generic cute animal sounds"

#Luokka toteuttaa ylemmän luokan ottamalla sen parametrikseen
class Lion(Animal):
	#Luokan metodissa on oltava parametrina self, joka viittaa olioon,
        #jossa metodia suoritetaan
	def sound(self):
        return "Rooaar!"

#Main metodi suorittaa varsinaisen ohjelman
def main():
    lion = Lion()
    print(lion.sound())

if __name__ == "__main__":
    main()

