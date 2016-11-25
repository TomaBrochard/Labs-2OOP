
import os
import random
from Plateau import *

class Bateau:
	""" Bateau de Bataille Navale comportant un plateau, une lettre d'affichage, ses coordonées,
	uneorientation, une taille , des vies et 2 bool pour savoir si il est placé et coulé"""

	def __init__(self, plateau, lettre, taille, nom="bateau", aleatoire=False, vitesse=1):
		""" Constructeur """
		self.__plateau = plateau
		self.__lettre = lettre
		self.__place = False
		self.__taille = taille
		self.__vie = taille
		self.__estCoulle = False
		self.__coords = [0,0]
		self.__orientation = 0    # 0 = bateau verticale, 1 = bateau horizontale
		self.__nom = nom
		self.__vitesse = vitesse

		if aleatoire:
			self.placerRandom()
		else:
			self.demanderCoords()
		# s'écrit aussi:
		#self.placerRandom() if aleatoire else self.demanderCoords()

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
	def estplace(self):
		return self.__place
	def getNom(self):
		return self.__nom
	def estCoulle(self):
		return self.__estCoulle
	def getVitesse(self):
		return self.__vitesse


	# SETTERS
	def setOrientation(self, new):
		if new == 0 or new == 1:
			self.__orientation = new

	def placer(self, coords, orientation):
		""" Place le bateau sur le plateau (setter cumulé de coords, orientation et place) """

		# si la place est libre on place le bateau,sinon on retourne False
		if self.getPlateau().estLibre(coords, orientation, self.getTaille()):
			self.__coords = coords
			self.__orientation = orientation
			for i in range (self.getTaille()):
				self.getPlateau().setCase(coords[0] + i *  orientation,
									  	  coords[1] + i * ((orientation+1)%2),
									  	  self.getLettre())
			self.__place = True
		return self.estplace()

	def retirer(self):
		""" retire le bateau du plateau (setter cumulé de coords, orientation et place) """
		for i in range(self.getTaille()):
			self.getPlateau().setCase(self.getCoord(0) + i *  self.getOrientation(),
									  self.getCoord(1) + i * ((self.getOrientation() + 1) % 2),
									  '.')
		self.__place = False

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
								 	  self.getCoord(1) + i * ((self.getOrientation()+1)%2),
									  'c')


	def demanderCoords(self):
		""" affiche le plateau du joueur pour qu'il visualise ses bateaux et lui demande leur coordonnées"""
		legal = False

		# On affiche le plateau pour que le joueur sache ou il place son bateau
		os.system("cls")
		print("      A  B  C  D  E  F  G  H  I  J       \n")
		self.getPlateau().affiche()
		print()

		while not legal:
			# On lui demande ou il veux le placer
			coordsOri = self.__getUsableCoords()
			if self.placer(coordsOri[0], coordsOri[1]):
				legal = True
				self.__confirmePlacement()
			else:
				print("Placement du " + self.getNom() + " incorrecte")

	def __getUsableCoords(self):
		""" Demande les coordoné du bateau et les renvoi en les convertissant via la table ascii """
		rawCoords = input("Entrez les coordonnees de l'avant du "+ self.getNom() +" ("+ str(self.getTaille()) +" cases) : ")
		coordOri = [[]]  # ici coordOri contien ligne, colonne dans une liste et orientation
		coordsLegal = False
		orientLegal = False

		# l'input utilisateur est limité à deux caractéres
		if len(rawCoords) == 2:
			for i in range(2):

				# on récupére la valeur ascii de chaque caractére avec ord()
				coordOri[0].append(ord(rawCoords[i]))

				# si le caractére est en minuscule, le mettre en majuscule
				if coordOri[0][i] in range(97, 123):
					coordOri[0][i] -= 32

			# On trie et on inverse la liste pour avoir [chiffre,lettre] donc [ligne, colonne]
			coordOri[0].sort()

			# On accepte que les lettres de A à J (65 - 75) et les chifres de 0 à 9 (65 - 75)
			if coordOri[0][0] in range(48, 58) and coordOri[0][1] in range(65, 75):
				# transforme les lignes et les colonnes pour obtenir un int entre 0 et 9 facilement utilisable
				coordOri[0][0] -= 48
				coordOri[0][1] -= 65
				coordsLegal = True
		if coordsLegal:
			while not orientLegal:
				rawOrient = input("Entrez l'orientation du Bateau (vertical/horizontal): ").upper()
				if rawOrient in ["0", "V","VERT", "VERTI","VERTICAL"]:
					orientLegal = True
					coordOri.append(1)
				else:
					if rawOrient in ["1", "H","HOR", "HORI","HORIZ", "HORIZON","HORIZONTAL"]:
						orientLegal = True
						coordOri.append(0)
					else:
						print("Incorect, merci de saisire 'v' pour vertical ou 'h' pour horizontal")
			return coordOri
		else:
			print("Incorect, merci de saisire une ligne [0-9] et une colonne [A-J] ")
			return self.__getUsableCoords()

	def __confirmePlacement(self):
		""" affiche le plateau du joueur avec son bateau placé et lui demande confirmation """
		legal = False

		# On affiche le plateau pour que le joueur sache ou il place son bateau
		os.system("cls")
		print("      A  B  C  D  E  F  G  H  I  J       \n")
		self.getPlateau().affiche()
		print()

		while not legal:

			# On lui demande confirmation
			rawConfirmation = input("Votre " + self.getNom() + " est placé, cela vous convient il ? [O/n]").upper()

			# Si il répond oui ou non, la saisie est legal
			if rawConfirmation in ["N","NO","NON","NOPE"] or rawConfirmation in ["O","Y","YES","OUI", ""]:
				legal = True

				# Si il répond non, on retire le bateau du plateau et on lui redemande
				if rawConfirmation in ["N","NO","NON","NOPE"]:
					self.retirer()
					self.demanderCoords()
				# Si il répond oui, le bateau est deja placé, rien de plus se passe

			# Sinon si il répond autre chose, la réponse est incorecte, on lui redemande confirmation
			else:
				print("Incorect, merci de saisire oui ou non")

	def placerRandom(self):
		""" position aleatoire du Bateau puis test si il y a superposition. Si c'est bon: placer
		 sinon deplacer le bateau en parallelle. Si toujour pas, boucler """
		orientation = random.randrange(0, 2)  # 0 = bateau verticale, 1 = bateau horizontale
		coords = [random.randrange(0, self.getPlateau().getLenLigne()   - self.getTaille() *  orientation),
				  random.randrange(0, self.getPlateau().getLenColonne() - self.getTaille() * (orientation+1)%2)]

		# On essay de placer le bateau,si c'est vrais il est placé si c'est faux, on reteste en le deplacant sur son flanc
		if not self.placer(coords, orientation):
			for i in range(1, 10):
				if self.placer([(coords[0] + i *  orientation       ) % 10,
								(coords[1] + i * ((orientation + 1)%2)) % 10],
							     orientation):
					break

		# si a ce stade le bateau n'est toujours pas placé, c'est que toute les places
		# parralelle à lui meme sont prises, donc on relance le placement random.
		if not self.estplace():
			self.placerRandom()

	def deplacer(self, sense=1):
		""" fait avancer le Bateau selon son orientation (en haut pour verticale ou à gauche pour horizontal"""
		coordsDestination = [self.getCoord(0) + sense * self.getVitesse() *   self.getOrientation(),
							 self.getCoord(1) + sense * self.getVitesse() * ((self.getOrientation()+1)%2)]
		autreBateau = Plateau.bateau.copy()
		autreBateau.remove(self.getLettre())
		if self.getPlateau().estLibre(coordsDestination, self.getOrientation(), self.getTaille(), autreBateau):
			self.retirer()
			self.placer(coordsDestination, self.getOrientation())
			return True
		else:
			print("Impossible " + ("d'avancer" if sense>0 else "de reculer"))
			return False


class Porte_avions(Bateau):
	""" Classe héritant de Bateau avec une taille de 5 et est noté 'P' """

	def __init__(self, plateau, aleatoire=False):
		""" Constructeur """
		super().__init__(plateau, 'P', 5, "porte avion", aleatoire)

class Croiseur(Bateau):

	def __init__(self, plateau, aleatoire=False):
		""" Constructeur """
		Bateau.__init__(self, plateau, 'C', 4, "croiseur", aleatoire)

class Contre_torpilleur(Bateau):

	def __init__(self, plateau, aleatoire=False):
		""" Constructeur """
		super().__init__(plateau, 'U', 3, "contre torpilleur", aleatoire)

class Sous_marin(Bateau):

	def __init__(self, plateau, aleatoire=False):
		""" Constructeur """
		Bateau.__init__(self,plateau, 'S', 3, "sous-marin", aleatoire)
		self.__plonge = False

	def estPlonge(self):
		return self.__plonge

	def plonger(self):
		""" Fait plonger le sous-marin, il réaparaitra apres le tour suivant. """
		if not self.__plonge:
			self.retirer()
			self.__plonge = True

	def remonter(self):
		""" le sous-marin remonte """
		if self.__plonge:
			self.placer(self.getCoords(), self.getOrientation())
			self.__plonge = False

class Torpilleur(Bateau):

	def __init__(self, plateau, aleatoire=False):
		""" Constructeur """
		super().__init__(plateau, 'T', 2, "torpilleur", aleatoire)
