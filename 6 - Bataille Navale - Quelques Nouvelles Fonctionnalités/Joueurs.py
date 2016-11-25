import os
from Plateau import *
from Bateau import *

class Joueurs:
	""" Joueur de Bataille Navale possédant un nom, un plateau et des Bateaux """
	nbJoueurs = 0
	def __init__(self):
		""" Constructeur """
		self.__nom = self.demanderNom()
		self.__plateau = Plateau()
		aleatoire = self.demanderPlacementBateau()
		self.__flotte = [Porte_avions(self.__plateau, aleatoire), Croiseur(self.__plateau, aleatoire),
						 Contre_torpilleur(self.__plateau, aleatoire), Sous_marin(self.__plateau, aleatoire),
						 Torpilleur(self.__plateau, aleatoire)]
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

	@classmethod
	def demanderNom(cls, taille_max=30):
		""" demande son nom au joueur """
		cls.nbJoueurs+=1
		os.system("cls")
		nom = input("Entrez le nom du joueur " + str(cls.nbJoueurs) + " : ")
		if len(nom) <= taille_max:
			return nom
		else:
			print("veuillez entrer un nom de moins de " + str(taille_max) + " carracteres")
			return cls.demanderNom(taille_max)

	@classmethod
	def RAZNbJoueurs(cls):
		""" Remet le nombre de joueurs à 0 au cas au le joueur souhaite rejouer """
		cls.nbJoueurs = 0

	def demanderPlacementBateau(self):
		""" Demande si le joueur souhaite placer ses Bateau aléatoirement (plus rapide) """
		placement = input("Voulez vous placer vos Bateaux aleatoirement ? [O/n]").upper()
		if placement in ["", "O", "Y", "OUI", "YES", "YEP"] or placement in ["N", "NO", "NON"]:
			if placement in ["N", "NO", "NON"]:
				return False
			else:
				return True
		else:
			print("Incorect, merci de saisire oui ou non")
			return self.demanderPlacementBateau()

	def demanderCoordonnees(self):
		"""demande les coordoné et les renvoi en les convertissant via la table ascii"""
		rawCoords = input("Entrez les coordonnees du tire : ")
		coords = []

		# l'input utilisateur est limité à deux caractéres
		if len(rawCoords) == 2:

			# Si lejoueur entre 42, il gagne automatiquement, (pour tester l'écran de fin)
			if rawCoords == "42":
				self.gagne()
				return 42
			for i in range(2):

				# on récupére la valeur ascii de chaque caractére avec ord()
				coords.append(ord(rawCoords[i]))

				# si le caractére est en minuscule, le mettre en majuscule
				if coords[i] in range(97, 123):
					coords[i] -= 32

			# On trie la liste pour avoir [chiffre, lettre] donc [ligne, colonne]
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

	def deplacerBateau(self, sense=1):
		""" demande au joueur quel bateau il veux déplacer et le fait """
		print()
		rawBateau = input(" 1: Porte-avion\n"
						  " 2: Croiseur\n"
						  " 3: Contre-torpilleur\n"
						  " 4: Sous-marin\n"
						  " 5: Torpilleur\n"
						  "Quel bateau voulez vous deplacer ? : ").upper()
		if rawBateau in ["1", "PORTE-AVION", "2", "CROISEUR", "3", "CONTRE-TORPILLEUR",
						 "4", "SOUS-MARIN", "5", "TORPILLEUR"]:
			resultat = False
			if rawBateau in ["1", "PORTE-AVION"]:
				resultat = self.getBateau(0).deplacer(sense)
			elif rawBateau in ["2", "CROISEUR"]:
				resultat = self.getBateau(1).deplacer(sense)
			elif rawBateau in ["3", "CONTRE-TORPILLEUR"]:
				resultat = self.getBateau(2).deplacer(sense)
			elif rawBateau in ["4", "SOUS-MARIN"]:
				resultat = self.getBateau(3).deplacer(sense)
			elif rawBateau in ["5", "TORPILLEUR"]:
				resultat = self.getBateau(4).deplacer(sense)
			if resultat:
				return self.getNom() + " a déplacé un bateau."
			else:
				return self.deplacerBateau()
		else:
			print("Saisie incorrecte, veuillez saisire 1, 2, 3, 4 ou 5.")
			return self.deplacerBateau(sense)

	def plongerSousMarin(self):
		""" Fait plonger le sous-marin du joueur """
		self.getBateau(3).plonger()
		return self.getNom() + " a fait plonger son sous-marin."