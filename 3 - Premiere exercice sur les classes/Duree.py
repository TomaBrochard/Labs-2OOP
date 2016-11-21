
class Duree:

	def __init__(self, h=0, m=0, s=0):
		""" Constructeur & constructeur par défaut """
		self.__heures   = int(((s/60 + m)/60) + h)
		self.__minutes  = int ((s/60 + m)%60)
		self.__secondes = int  (s%60)


	def afficheDuree(self):
		""" Affiche la durée sous forme 0h00m00s """
		print("{}h{}m{}s"
			.format(self.getHeures(),
			("0" if self.getMinutes() <10 else "")+str(self.getMinutes ()),
			("0" if self.getSecondes()<10 else "")+str(self.getSecondes())))


	#####     Setters     #####
	def setHeures(self, new):
		""" Setter de heures """
		self.__heures = new

	def setMinutes(self, new):
		""" Setter de minutes """
		self.__minutes = new

	def setSecondes(self, new):
		""" Setter de secondes """
		self.__secondes = new


	#####     Getters     #####
	def getHeures(self):
		""" Getter de heures """
		return self.__heures

	def getMinutes(self):
		""" Getter de minutes """
		return self.__minutes

	def getSecondes(self):
		""" Getter de secondes """
		return self.__secondes


	def getDureeToSecondes(self):
		""" Retourne la valeur de la durée en secondes """
		return self.getHeures()*3600 + self.getMinutes()*60 + self.getHeures()

	def addSecondes(self, sec):
		""" Ajoute à la durée un nombre de seconde passé en paramètre """
		self.setHeures  (int((((self.getSecondes() + sec)/60 + self.getMinutes())/60) + self.getHeures()))
		self.setMinutes (int (((self.getSecondes() + sec)/60 + self.getMinutes())%60))
		self.setSecondes(      (self.getSecondes() + sec)%60)

class DureeBis:
	# Fonctionnement alternatif plus lisible mais plus coûteux en ressources

	def __init__(self, h=0, m=0, s=0):
		""" Constructeur & constructeur par défaut """
		self.__heures, self.__minutes, self.__secondes = 0,0,0
		self.setHeures(h)
		self.setMinutes(m)
		self.setSecondes(s)

	def afficheDuree(self):
		""" Affiche la durée sous forme 0h00m00s """
		print("{}h{}m{}s"
			.format(self.getHeures(),
			("0" if self.getMinutes() <10 else "")+str(self.getMinutes ()),
			("0" if self.getSecondes()<10 else "")+str(self.getSecondes())))


	#####     Setters     #####
	def setHeures(self, new):
		""" Setter de heures """
		self.__heures = new

	def setMinutes(self, new):
		""" Setter de minutes """
		self.__minutes = new%60
		self.setHeures(self.getHeures() + int(new/60))

	def setSecondes(self, new):
		""" Setter de secondes """
		self.__secondes = new%60
		self.setMinutes(self.getMinutes() + int(new/60))


	#####     Getters     #####
	def getHeures(self):
		""" Getter de heures """
		return self.__heures

	def getMinutes(self):
		""" Getter de minutes """
		return self.__minutes

	def getSecondes(self):
		""" Getter de secondes """
		return self.__secondes


	def getDureeToSecondes(self):
		""" Retourne la valeur de la durée en secondes """
		return self.getHeures()*3600 + self.getMinutes()*60 + self.getHeures()

	def addSecondes(self, sec):
		""" Ajoute à la durée un nombre de seconde passé en paramètre """
		self.setSecondes(self.getSecondes() + sec)


if __name__ == '__main__':
	a = Duree(1,0,0)
	a.afficheDuree()
	a.addSecondes(61)
	a.afficheDuree()
	a.addSecondes(5635)
	a.afficheDuree()
	print()
	b = Duree(999,59,59)
	b.afficheDuree()
	b.addSecondes(1)
	b.afficheDuree()

	print()
	print()

	c = DureeBis(1,0,0)
	c.afficheDuree()
	c.addSecondes(61)
	c.afficheDuree()
	c.addSecondes(5635)
	c.afficheDuree()
	print()
	d = DureeBis(0,0,4000)
	d.afficheDuree()
	d.addSecondes(1)
	d.afficheDuree()