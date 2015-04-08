#!/usr/bin/python
# -*- coding: utf-8 -*
###########################################################################################
#personaje
class champion:
	"""Create champion"""
	def __init__(self,name,tipe):
		self.name=name
		self.attributes=["vitality","stamina","strength","defense","agility","magic","resistance"]
		self.attvalues=[0,0,0,0,0,0,0]
		self.lvl=0
		self.tipe=tipe
		self.lvlexp=50*self.lvl
		self.exp=0
	def lvlup(self,attup):
		for att in range(len(self.attvalues)):
			self.attvalues[att]+=attup[att]
	def lvluptipe(self):
		if self.tipe == "warrior":
			attup=[50,50,5,2,2,0,1]
			self.lvlup(attup)
				
		elif self.tipe == "guardian":
			attup=[75,25,2,4,1,0,3]
			self.lvlup(attup)

		elif self.tipe == "assassin":
			attup=[25,75,4,1,4,0,1]
			self.lvlup(attup)

		elif self.tipe == "mage":
			attup=[25,75,0,1,1,5,3]
			self.lvlup(attup)

		elif self.tipe == "antimage":
			attup=[75,25,3,1,2,0,4]
			self.lvlup(attup)

	def showatt(self):
		for att in range(len(self.attributes)):
			print self.attributes[att],self.attvalues[att]
		print("\n")
	def checklvl(self):
		if self.exp>=self.lvlexp:
			self.lvl+=1
			self.exp=0+(self.exp-self.lvlexp)
			self.lvlexp=50*self.lvl
			self.lvluptipe()
			print "\nLevel up! Lvl", self.lvl
			self.showatt()

#########################################################################################
#enemigos
class enemy:
	"""Create enemy"""
	def __init__(self,ratio,lvl,tipe):
		self.attributes = ["vitality","stamina","strength","defense","agility","magic","resistance"]
		self.attvalues = [0,0,0,0,0,0,0]
		self.lvl = lvl
		self.ratio = ratio
		self.exp = 20*ratio*lvl
		self.tipe = tipe

	def lvlup(self):
		for att in range(len(self.attvalues)):
			self.attvalues[att] *= self.ratio* self.lvl

	def lvluptipe(self):
		if self.tipe == "warrior":
			self.attvalues = [20,20,3,1,1,0,0]
			self.lvlup()
				
		elif self.tipe == "guardian":
			self.attvalues=[30,10,2,3,1,0,2]
			self.lvlup()

		elif self.tipe == "assassin":
			self.attvalues =[10,30,6,0,3,0,0]
			self.lvlup()

		elif self.tipe == "mage":
			self.attvalues =[15,35,1,1,1,5,3]
			self.lvlup()

		elif self.tipe == "antimage":
			self.attvalues = [25,15,3,1,2,0,4]
			self.lvlup()

	def showatt(self):
		for att in range(len(self.attributes)):
			print self.attributes[att],self.attvalues[att]


def createuser():
	"""Function to create a character"""
	name = raw_input("Hello! Write your character's name! ")
	tipe = raw_input("Now your character's profession! ")

	user = champion(name,tipe)
	user.checklvl()
	return(user)