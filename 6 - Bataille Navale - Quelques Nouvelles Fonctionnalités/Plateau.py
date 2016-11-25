
class Plateau(list):
	""" Plateau de Bataille Navale en 10x10 """

	bateau = ['P', 'C', 'S', 'U', 'T', False]

	def __init__(self, ligne=10, colonne=10):
		""" Constructeur """
		# on construit le plateau qui sera un tableau à 2 dimension remplie de '.'*
		super().__init__()
		for i in range(ligne):
			self.append([])
			for j in range(colonne):
				self[i].append('.')

	# GETTERS
	def getCase(self, ligne, colonne):
		if ligne < self.getLenLigne() and colonne < self.getLenColonne():
			return self[ligne][colonne]
		else:
			return False

	def getLenLigne(self):
		return len(self)
	def getLenColonne(self):
		return len(self[0])

	# SETTERS
	def setCase(self, ligne, colonne, new):
		if ligne < self.getLenLigne() and colonne < self.getLenColonne():
			self[ligne][colonne]= new



	def affiche(self, cache=False):
		""" Appelle afficheLigne() pour chaque lignes du Plateau """
		for i in range(self.getLenLigne()):
			print(' ' + str(i), end='    ')
			self.afficheLigne(i, cache)
			print()

	def afficheLigne(self, ligne, cache=False):
		""" Appelle afficheCase() pour chaque cases de la ligne """
		for i in range(self.getLenColonne()):
			self.afficheCase(ligne, i, cache)

	def afficheCase(self, ligne, colonne, cache=False):
		""" Print le contenu de la case en question ou un '.' si elle est caché (plateau adversaire) """
		case = str(self.getCase(ligne, colonne))

		# Si une case contient un bateau et est caché, on affiche '.' sinon onaffiche le bateau
		if cache and case in self.bateau:
			print ('.', end='  ')
		else:
			print (case, end='  ')

	def estLibre(self, coords, orientation, taille=1, exclusion=bateau):
		""" test si la place sur le plateau est libre """
		for i in range(taille):
			if self.getCase(coords[0] + i * orientation, coords[1] + i * ((orientation+1)%2)) in exclusion:
				return False
		return True