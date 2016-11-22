
class Plateau:

	bateau = ['P', 'C', 'S', 'U', 'T']

	def __init__(self):
		pass

	def getCase(self, ligne, colonne):
		pass
	def setCase(self, ligne, colonne, new):
		pass

	def __estLibre(self, coords, orientation, taille):
		""" test si la place sur le plateau est libre """
		for i in range(taille):
			if self.getCase(coords[0] + i * orientation,
							coords[1] + i * (orientation+1)%2) in self.bateau:
				return False
		return True

	def placerBateau(self, coords, orientation, taille, lettre):
		""" si la place est libre, place un bateau en inscrivant sa lettre à sa place """
		if self.__estLibre( coords, orientation, taille):
			for i in range(taille):
				self.setCase(coords[0] + i * orientation,
							 coords[1] + i * (orientation + 1) % 2,
							 lettre)
			return True
		else:
			return False
