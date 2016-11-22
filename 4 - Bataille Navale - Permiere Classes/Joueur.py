from Plateau import *
from Bateau import *

class Joueurs:
	""" Joueur de Bataille Navale possédant un nom, un plateau et des Bateaux """

	def __init__(self, nom = "Joueur 1"):
		""" Constructeur """
		self.__nom = nom
		self.__plateau = Plateau()
		self.__flotte = [Porte_avions(self.__plateau), Croiseur(self.__plateau),
					   Contre_torpilleur(self.__plateau), Sous_marin(self.__plateau),
					   Torpilleur(self.__plateau)]
		self.__vainceur = False

	# GETTERS
	def getNom(self):
		return self.__nom
	def getPlateau(self):
		return self.__plateau
	def getFlotte(self):
		return self.__flotte
	def getBateau(self, index):
		return self.__flotte[index]
	def estVainceur(self):
		return self.__vainceur

	# SETTERS
	def gagne(self):
		""" setter de vainceur, on ne peut que gagner """
		self.__vainceur = True

	def demanderCoordonnees(self):
		"""demande les coordoné et les renvoi en les convertissant via la table ascii"""
		rawCoords = input("Entrez les coordonnees du tire : ")
		coords = []


		# l'input utilisateur est limité à deux caractéres
		if len(rawCoords) == 2:
			# si le joueur entre 42, il gagne, pour tester l'écrant de fin.
			if rawCoords == "42":
				self.gagne()
				return 42
			else:
				for i in range(2):

					# on récupére la valeur ascii de chaque caractére avec ord()
					coords.append(ord(rawCoords[i]))

					# si le caractére est en minuscule, le mettre en majuscule
					if coords[i] in range(97, 123):
						coords[i] -= 32

				# On trie et on inverse la liste pour avoir [lettre, chiffre] donc [ligne, colonne]
				coords.sort()

				# On accepte que les chifres de 0 à 9 (48, 58) et les lettres de A à J (65 - 75)
				if coords[0] in range(48, 58) and coords[1] in range(65, 75):

					# transforme les lignes et les colonnes pour obtenir un int entre 0 et 9 facilement utilisable
					coords[0] -= 48
					coords[1] -= 65
					return coords

		# si on arrive à c stade, le programme n'est pas passé dans le return donc la saisie est incorect
		print("Incorect, merci de saisire une ligne [0-9] et une colonne [A-J] ")
		return self.demanderCoordonnees()