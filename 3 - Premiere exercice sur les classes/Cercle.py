from math import sqrt

class Cercle:
	pi = 3.14159

	def __init__(self, r=1, absol=0, ordon=0):
		""" Constructeur & constructeur par défaut """
		self.__rayon = abs(r)
		self.__abscisse = absol
		self.__ordonnee = ordon


	def aire(self):
		""" Calcule et retourne l'aire d'un cercle """
		return self.pi * self.__rayon * self.__rayon  # On peut aussi utiliser sqrt() de la Bibliotheque math

	def perimetre(self):
		""" Calcule et retourne le périmetre d'un cercle """
		return 2 * self.pi * self.__rayon

	def afficheCoords(self):
		""" Affiche les coordonnées du centre et le rayon """
		print("Cercle de centre d'abscisse: {}, d'ordonnee: {} et de rayon: {}."
			  .format(self.getAbscisse(), self.getOrdonnee(), self.getRayon()))


	#####     Setters     #####
	def	setRayon(self, new):
		""" Setter de rayon """
		self.__rayon = abs(new)

	def	setAbscisse(self, new):
		""" Setter de abscisse """
		self.__abscisse = new

	def	setOrdonnee(self, new):
		""" Setter de ordonnee """
		self.__ordonnee = new


	#####     Getters     #####
	def	getRayon(self):
		""" Getter de rayon """
		return self.__rayon

	def	getAbscisse(self):
		""" Getter de abscisse """
		return self.__abscisse

	def	getOrdonnee(self):
		""" Getter de ordonnee """
		return self.__ordonnee


	def contient(self, x, y):
		""" Renvoi vrais si le point dont les coordonnées passé en paramètre est dans le cercle """
		distanceDuCentre = sqrt( (self.getAbscisse()-x)**2 + (self.getOrdonnee()-y)**2 )
		return distanceDuCentre < self.getRayon()

	def translation(self, x, y):
		""" Réalise une translation selon les coordonées d"un vecteur passé en paramètre """
		self.setAbscisse(self.getAbscisse()+x)
		self.setOrdonnee(self.getOrdonnee()+y)

	def homothetie(self, k):
		""" Réalise l'omotethetie du cercle en fonction d'un facteur passé en paramètre """
		self.setAbscisse(self.getAbscisse()*k)
		self.setOrdonnee(self.getOrdonnee()*k)
		self.setRayon(self.getRayon()*k)		# on peu ne pes se soucier du signe car il est deja gérè dans le setter




if __name__ == '__main__':

	a = Cercle(5,5,5)

	a.afficheCoords()
	print(a.aire())
	print(a.perimetre())
	print(a.contient(4, 4))
	print(a.contient(0, 0))
	print()

	a.translation(-10,0)
	a.afficheCoords()
	print(a.aire())
	print(a.perimetre())
	print(a.contient(-4, 4))
	print(a.contient(0, 0))
	print()

	a.homothetie(-3)
	a.afficheCoords()
	print(a.aire())
	print(a.perimetre())
	print(a.contient(-8, 8))
	print(a.contient(0, 0))
