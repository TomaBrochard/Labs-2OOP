import os
from Joueurs import *

class BatailleNavale:
	""" Jeu de bataille Navale sur des plateau de 10x10 avec 5 types de bateaux"""
	casePossible = ['.','P','C','S','U','T', 'w', 't', 'c']

	def __init__(self):
		""" constructeur """
		self.__joueurs = list()
		self.commencerJeu()

	# GETTERS
	def getJoueur(self, index):
		if index == 0 or index == 1:
			return self.__joueurs[index]

	# SETTERS
	def setJoueur(self,index, new):
		self.__joueurs[index] = new
	def setJoueurs(self,new):
		self.__joueurs = new

	def commencerJeu(self):
		""" Routine principale du jeu """

		os.system("color  F0")
		# On instancie les joueurs ici pour pouvoir en changer en cas de nouvelle partie
		self.setJoueurs([Joueurs(self.demanderNom()),
						 Joueurs(self.demanderNom('2'))])

		# tant qu'il n'y a pas de vainceurs, on joue
		while self.getJoueur(0).estVainceur() == False and self.getJoueur(1).estVainceur() == False:
			self.afficheJeu()
			self.tirer()

		# normalement à ce stade, d'est joueurs[1] qui à gagné car il vient de tirer et on a changé de tour
		self.rejouer(self.getJoueur(1))

	def rejouer(self, gagnant):
		""" Affiche l'écran "récompense" et demande si les joueurs veulent rejouer """
		os.system("cls")
		print("\n  " + gagnant.getNom() + " a gagne, bravo !", end='\n \n \n')
		print("\t     ____________________________________       \n" +
			  "\t     |\_________________________________/|\     \n" +
			  "\t     ||                                 || \    \n" +
			  "\t     ||  __   __    __  _      _  ___   ||  \   \n" +
			  "\t     || |  \ |  \  //\\\ \\\    // / _ \  ||  | \n" +
			  "\t     || |  / |  / ||__|| \\\  // | / \ | ||  |  \n" +
			  "\t     || |  \ ||\\\ ||--||  \\\//  | \_/ | ||  | \n" +
			  "\t     || |__/ || \\\||  ||   \/    \___/  ||  |  \n" +
			  "\t     ||            __   __              ||  |   \n" +
			  "\t     ||     °-=,__/  \_/  \__,=-°       ||  /   \n" +
			  "\t     ||_________________________________|| /|   \n" +
			  "\t     |/_________________________________\|/ |   \n" +
			  "\t     |__\_____________________________/__| /    \n" +
			  "\t     |___________________________________|/     \n" +
			  "\t     ____________________________________       \n" +
			  "\t    /o  oooo  oooo  oooo  oooo  ooo    / |      \n" +
			  "\t   /oooooooooooooooooooooooooo ooo ooo/ /       \n" +
			  "\t  /oooooooooooooooooooooooooo ooo ooo/ /        \n" +
			  "\t /oooooooooooooooooooooooooo ooo ooo/_/         \n" +
			  "\t/__________________________________/_/          \n")

		# on demande s'il veux rejouer et on passe la réponse en maj pour ne pas avoir a traiter min et maj
		rejouer = input("Voulez vous rejouer ? (O/n)").upper()
		if rejouer in ["", "O", "Y", "OUI", "YES", "OK"]:
			os.system("cls")
			self.commencerJeu()
		else:
			if rejouer in ["N", "NON", "NO"]:
				exit() # termine le programme et ferme la console

	def tirer(self):
		""" demande au joueur où il veux tirer et évalue son tire """

		# coords contient les coordonées entré par le joueur
		coords = self.getJoueur(0).demanderCoordonnees()

		# si le joueur entre 42, il gagne, pour tester l'écrant de fin.
		if coords == 42:
			return True
		# cible contient la lettre de la case visé
		cible = self.getJoueur(0).getPlateau().getCase(coords[0], coords[1])
		# case correspond à l'index de cible dans casPossible, plus facile à manipuler (int)
		case = self.casePossible.index(cible)

		# Si le joueur a deja tiré ici, on lui dit et il re-tire
		if  case > 5:
			print("cible deja touchee")
			self.tirer()
		else:
			if case == 0:                                                   # dans l'eau
				self.getJoueur(1).getPlateau().setCase(coords[0], coords[1], 'w')
				self.changerTour(coords, case)
			else:                                                           # touché
				self.getJoueur(1).getPlateau().setCase(coords[0], coords[1], 't')

				# on décrémente une vie au bateau ce qui entraine de le couler s'il n'en a plus
				self.getJoueur(1).getBateau(case-1).decrementerVie()
				self.changerTour(coords, case)

	def changerTour(self, coor, cible):
		""" affiche le coup joué et marque une pause pour changer de joueur """
		resultat = ["Dans l'eau",						# la case ciblé était '.'
					'Porte-avion touche',				# la case ciblé était 'P'
					'Croiseur touche',					# la case ciblé était 'C'
					'Contre-torpilleur touche',			# la case ciblé était 'U'
					'Sous-marin touche',				# la case ciblé était 'S'
					'Torpilleur touche',				# la case ciblé était 'T'
					None, None, None]					# la case ciblé était 'w', 't' ou 'c' ce qui n'est pas permis mais on sait jamais
		__colonnes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

		#On utilise une variable str pour créer la texte qu'on affichera aprés
		affiche = self.getJoueur(0).getNom() + " a tiré en " + __colonnes[int(coor[0])] + str(coor[1]) + " : " + resultat[cible]
		if self.getJoueur(1).getBateau(cible-1).estCoulle():
			affiche += ", coulee."

			# On verifie si le joueur adverse a encore des bateaux non coulé sinon le joueur gagne
			gagne = True
			for i in range(self.getJoueur(1).getFlotte()):
				if not i.estCoulle():
					gagne = False
			if gagne:
				self.getJoueur(0).estVainceur = True
		else:
			affiche += "."

		# On échange la place des joueurs
		_tampon = self.getJoueur(0)
		self.setJoueurs(0, self.getJoueur(1))
		self.setJoueurs(1, _tampon)

		# On réalise l'affichage du coup joué
		affiche += "\n \n Au tour de "+ self.__joueurs[0].nom
		os.system("cls")
		print(affiche)
		# On marque une pause pour pas qu'un joueur puisse voire le plateau de l'autre
		input()

	def afficheJeu(self):
		""" affichage principale sur lequel on vois son plateau et le
		plateau de l'adversaire caché (on ne vois que ses tires) """
		os.system("cls")
		print("      A  B  C  D  E  F  G  H  I  J       |      A  B  C  D  E  F  G  H  I  J\n")

		# affiche plateaux l'un a coté de l'autre en altérnant les lignes des deux joueurs
		for i in range(10):
			print(' ' + str(i), end='    ')
			self.getJoueur(0).getPlateau().afficheLigne(i)
			print('     |      ', end='')
			self.getJoueur(0).getPlateau().afficheLigne(i, cache=True)
			print(str(i) + '\n')

		# affiche nom des joueurs centré (max 35 caractéres)
		for i in range(int((38 - len(self.getJoueur(0).getNom())) / 2)):
			print(' ', end='')
		print(self.getJoueur(0).getNom(), end="")
		for i in range(int((39 - len(self.getJoueur(0).getNom())) / 2)):
			print(' ', end='')
		print('   |   ', end='')
		for i in range(int((30 - len(self.getJoueur(1).getNom())) / 2)):
			print(' ', end='')
		print(self.getJoueur(1).getNom(), '\n')

	def demanderNom(self, numJoueur='1', taille_max=30):
		""" demande son nom au joueur """
		nom = input("Entrez le nom du joueur " + numJoueur + " : ")
		if len(nom) <= taille_max:
			os.system("cls")
			return nom
		else:
			print("veuillez entrer un nom de moins de " + str(taille_max) + " carracteres")
			return self.demanderNom(numJoueur, taille_max)

if __name__ == '__main__':

	game = BatailleNavale()