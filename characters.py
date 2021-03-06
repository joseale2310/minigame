# -*- coding: utf-8 -*
###########################################################################################
#personaje
class champion:
	"""Create champion"""
	def __init__(self,name,tipe):
		self.name=name
		self.attributes=["HP","MP","Strength","Defense","Agility","Magic","Resistance","Accuracy"]
		self.attvalues=[0,0,0,0,0,0,0,0]
		self.lvl=1
		self.tipe=tipe
		self.lvlexp=50*self.lvl
		self.exp=0
		self.position=["laberinto.txt",1,19,1,19]
	def firstatt(self):
		if self.tipe == "warrior":
			attup=[50,50,10,5,2,0,1,0.8]
			self.lvlup(attup)
				
		elif self.tipe == "guardian":
			attup=[75,25,5,20,1,0,3,0.75]
			self.lvlup(attup)

		elif self.tipe == "assassin":
			attup=[25,75,7,2.5,4,0,1,0.9]
			self.lvlup(attup)

		elif self.tipe == "mage":
			attup=[25,75,0,10,1,5,3,0.8]
			self.lvlup(attup)

		elif self.tipe == "antimage":
			attup=[75,25,6,10,2,0,4,0.85]
			self.lvlup(attup)
		self.showatt()
	def lvlup(self,attup):
		for att in range(len(self.attvalues)):
			self.attvalues[att]+=attup[att]
	def lvluptipe(self):
		if self.tipe == "warrior":
			attup=[50,50,5,0.20,2,0,1,0.8]
			self.lvlup(attup)
				
		elif self.tipe == "guardian":
			attup=[75,25,2,0.5,1,0,3,0.85]
			self.lvlup(attup)

		elif self.tipe == "assassin":
			attup=[25,75,4,0.1,4,0,1,0.9]
			self.lvlup(attup)

		elif self.tipe == "mage":
			attup=[25,75,0,0.25,1,5,3,0.8]
			self.lvlup(attup)

		elif self.tipe == "antimage":
			attup=[75,25,3,0.25,2,0,4,0.85]
			self.lvlup(attup)

	def showatt(self):
		print ("Name:", self.name)
		print ("Profession:", self.tipe)
		print ("Level:", self.lvl, "Exp:", self.exp)
		for att in range(len(self.attributes)):
			print (self.attributes[att],self.attvalues[att])
			
	def checklvl(self):
		if self.exp>=self.lvlexp and self.lvl<=10:
			self.lvl+=1
			self.exp=0+(self.exp-self.lvlexp)
			self.lvlexp=50*self.lvl
			self.lvluptipe()
			print ("\nLevel up! Lvl", self.lvl,"\n")
			self.showatt()

####################################################
def createuser():
	"""Function to create a character"""
	name = input("Hello! Write your character's name! ")
	tipe = input("Now your character's profession!\nWarrior(1), Guardian(2), Assassin(3), Mage(4), Antimage(5): ")
	tipes=["warrior","guardian","assassin", "mage", "antimage"]
	print (tipe)
	user = champion(name,tipes[int(tipe)-1])
	user.firstatt()
	return(user)

#########################################################################################
#enemigos
class enemy:
	"""Create enemy"""
	def __init__(self,ratio,lvl,tipe):
		self.attributes = ["HP","MP","Strength","Defense","Agility","Magic","Resistance","Accuracy"]
		self.attvalues = [0,0,0,0,0,0,0,0]
		self.lvl = lvl
		self.ratio = ratio
		self.exp = 20*ratio*lvl
		self.tipe = tipe

	def lvlup(self):
		for att in range(len(self.attvalues)):
			self.attvalues[att] *= self.ratio * self.lvl

	def lvluptipe(self):
		if self.tipe == "warrior":
			self.attvalues = [20,20,5,1,1,0,0,0.6]
			self.lvlup()
				
		elif self.tipe == "guardian":
			self.attvalues=[30,10,3,3,1,0,2,0.5]
			self.lvlup()

		elif self.tipe == "assassin":
			self.attvalues =[10,30,8,0,3,0,0,0.8]
			self.lvlup()

		elif self.tipe == "mage":
			self.attvalues =[15,35,2,1,1,5,3,0.7]
			self.lvlup()

		elif self.tipe == "antimage":
			self.attvalues = [25,15,5,1,2,0,4,0.65]
			self.lvlup()

	def showatt(self):
		for att in range(len(self.attributes)):
			print (self.attributes[att],self.attvalues[att])


