import random

class Bateau:
	""" Bateau de Bataille Navale comportant un plateau, une lettre d'affichage, ses coordonées,
	uneorientation, une taille , des vies et 2 bool pour savoir si il est placé et coulé"""

	def __init__(self, plateau, lettre, taille):
		""" Constructeur """
		self.__plateau = plateau
		self.__lettre = lettre
		self.__place = False
		self.__taille = taille
		self.__vie = taille
		self.__estCoulle = False
		self.__coords = [0,0]
		self.__orientation = 0    # 0 = bateau verticale, 1 = bateau horizontale
		self.placerRandom()

	# GETTERS
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
	def estPlace(self):
		return self.__place
	def estCoule(self):
		return self.__estCoulle

	# SETTERS
	def setOrientation(self, new):
		if new == 0 or new == 1:
			self.__orientation = new
	def setCoords(self, new):
		self.__coords = new

	def placer(self, coords, orientation):
		""" Place le bateau sur le plateau (setter cumulé de coords, orientation et place"""

		# si la place est libre on place le bateau,sinon on retourne False
		if self.getPlateau().estLibre(coords, orientation, self.getTaille()):
			self.setCoords(coords)
			self.setOrientation(orientation)
			for i in range (self.getTaille()):
				self.getPlateau().setCase(coords[0] + i *  orientation,
									  	  coords[1] + i * (orientation+1)%2,
									  	  self.getLettre())
			self.__place = True
		return self.estPlace()

	def decrementerVie(self):
		""" décrémente une vie au bateau, s'il n'en a lus, il est coulé. Est un setter pour vie"""
		self.__vie -= 1

		# Si il n'a plus de vie, on coule le bateau
		if self.__vie == 0:
			self.couler()


	def couler(self):
		""" coulle le bateau, le remplace par des "c" sur le plateau. est le setter de estCoulle"""
		self.__estCoulle = True

		# remplace le bateau par des 'c' sur toute sa taille
		for i in range(self.getTaille()):
			self.getPlateau().setCase(self.getCoord(0) + i *  self.getOrientation(),
								 	  self.getCoord(1) + i * (self.getOrientation()+1)%2,
									  'c')

	def placerRandom(self):
		""" position aleatoire du Bateau puis test si il y a superposition. Si c'est bon: placer
		 sinon deplacer le bateau en parallelle. Si toujour pas, boucler """
		orientation = random.randrange(0, 2)  # 0 = bateau verticale, 1 = bateau horizontale

		# On créé les coordonées selon la taille et l'orientation du Bateau pour que le Bateau ne sorte pas du Tableau
		coords = [random.randrange(0, self.getPlateau().getLenLigne()   - self.getTaille() *  orientation),
				  random.randrange(0, self.getPlateau().getLenColonne() - self.getTaille() * (orientation+1)%2)]

		# On essay de placer le bateau,si c'est vrais il est placé si c'est faux, on reteste en le deplacant sur son flanc
		if not self.placer(coords, orientation):
			for i in range(1, 10):
				if self.placer([(coords[0] + i *  orientation       ) % 10,
								(coords[1] + i * (orientation + 1)%2) % 10],
							     orientation):
					break

		# si a ce stade le bateau n'est toujours pas placé, c'est que toute les places
		# parralelle à lui meme sont prises, donc on relance le placement random.
		if not self.estPlace():
			self.placerRandom()





class Porte_avions:
	def __init__(self, plateau):
		pass

class Croiseur:
	def __init__(self, plateau):
		pass

class Contre_torpilleur:
	def __init__(self, plateau):
		pass

class Sous_marin:
	def __init__(self, plateau):
		pass

class Torpilleur:
	def __init__(self, plateau):
		pass
