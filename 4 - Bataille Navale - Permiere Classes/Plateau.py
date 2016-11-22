class Plateau:
	""" Plateau de Bataille Navale en 10x10 """

	bateau = ['P', 'C', 'S', 'U', 'T']

	def __init__(self):
		""" Constructeur """
		# on construit le plateau qui sera un tableau à 2 dimension remplie de '.'
		self.__cases = list()
		for ligne in range(10):
			self.__cases.append([])
			for colonne in range (10):
				self.__cases[ligne].append('.')

	# GETTERS
	def getCase(self, ligne, colonne):
		return self.__cases[ligne][colonne]
	def getLenLigne(self):
		return len(self.__cases)
	def getLenColonne(self):
		return len(self.__cases[0])

	# SETTERS
	def setCase(self, ligne, colonne, new):
		self.__cases[ligne][colonne]= new



	def tirer(self, ligne, colonne):
		pass
	def afficheLigne(self, ligne, cache=False):
		""" Appelle afficheCase() pour chaque case de la ligne """
		for i in range(10):
			self.afficheCase(ligne, i, cache)

	def afficheCase(self, ligne, colonne, cache=False):
		""" Print le contenu de la case en question ou un '.' si elle est caché (plateau adversaire) """
		case = str(self.getCase(colonne, ligne))

		# Si une case contient un bateau et est caché, on affiche '.' sinon onaffiche le bateau
		if cache and case in self.bateau:
			print ('.', end='  ')
		else:
			print (case, end='  ')

	def estLibre(self, coords, orientation, taille=1, exclusion=bateau):
		""" test si la place sur le plateau est libre """
		for i in range(taille):
			if self.getCase(coords[0] + i * orientation, coords[1] + i * (orientation+1)%2) in exclusion:
				return False
		return True