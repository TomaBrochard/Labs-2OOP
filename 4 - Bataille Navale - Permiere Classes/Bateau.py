from random import randrange

class Bateau:
	""" Bateau de Bataille Navale comportant un plateau, une lettre d'affichage, ses coordonées,
		uneorientation, une taille , des vies et 2 bool pour savoir si il est placé et coulé"""
	def __init__(self, lettre, taille, plateau):
		""" Constructeur """
		self.__plateau = plateau
		self.__lettre = lettre
		self.__place = False
		self.__taille = taille
		self.__vie = taille
		self.__estCoulle = False
		self.__coords = [0, 0]
		self.__orientation = 0  # 0 = bateau verticale, 1 = bateau horizontale
		self.placerRandom()

	# Getters
	def getPlateau(self):
		return self.__plateau
	def getLettre(self):
		return self.__lettre
	def getCoords(self):
		return self.__coords
	def getCoord(self, index):
		if index == 0 or index == 1:
			return self.__coords[index]
	def getOrientation(self):
		return self.__orientation
	def getTaille(self):
		return self.__taille
	def getEstPlace(self):
		return self.__place

	# Setters
	def setOrientation(self, new):
		if new == 0 or new == 1:
			self.__orientation = new
	def setCoords(self, new):
		self.__coords = new
	def placer(self):
		self.__estPlace = True
	def decrementerVie(self):
		""" décrémente une vie au bateau, s'il n'en a lus, il est coulé. Est un setter pour vie"""
		self.__vie -= 1

		# Si il n'a plus de vie, on coule le bateau
		if self.__vie == 0:
			self.couler()



	def placerRandom(self):
		""" position aleatoire du Bateau puis test si il y a superposition. Si c'est bon: placer
				 sinon deplacer le bateau en parallelle. Si toujour pas, boucler """
		orientation = randrange(0, 2)  # 0 = bateau verticale, 1 = bateau horizontale

		# On créé les coordonées selon la taille et l'orientation du Bateau pour que le Bateau ne sorte pas du Tableau
		coordonnees = [ randrange(0, 10 - self.getTaille() * orientation),
						randrange(0, 10 - self.getTaille() * (orientation+1)%2) ]

		# On essay de placer le bateau,si c'est vrais il est placé
		if self.getPlateau().placerBateau(coordonnees,orientation, self.getTaille(), self.getLettre()):
			self.setOrientation(orientation)
			self.setCoords(coordonnees)
			self.placer()

		# si c'est faux, on reteste en le deplacant sur son flanc
		else:
			# on ne comence pas de 0 car on veux tester les 9 autre cases et pas les 10
			for i in range(1, 10):
				coordonnees = [(coordonnees[0] + i *  orientation) % 10,
							   (coordonnees[1] + i * (orientation+1)%2) % 10]
				if self.getPlateau().placerBateau(coordonnees, orientation, self.getTaille()):
					self.__orientation = orientation
					self.__coords = coordonnees
					self.placer()
					# break pour sortir du for
					break

		# Si le bateau n'est toujour pas placé, on relance le placement random
		if not self.getEstPlace():
			self.placerRandom()














