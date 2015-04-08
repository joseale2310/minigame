#!/usr/bin/python
# -*- coding: utf-8 -*
from subprocess import call
import getch
from random import random

#personaje
class champion:
	"""Create champion"""
	def __init__(self,name,tipe):
		self.name=name
		self.attributes=["vitality","stamina","strength","defense","agility","magic","resistance"]
		self.attvalues=[100,100,5,5,5,5,5]
		self.lvl=1
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
			attup=[25,75,3,1,4,0,2]
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


#enemigos
class enemy:
	"""Create enemy"""
	def __init__(self,ratio,lvl,tipe):
		self.attributes=["vitality","stamina","strength","defense","agility","magic","resistance"]
		self.attvalues=[0,0,0,0,0,0,0]
		self.lvl=lvl
		self.ratio=ratio
		self.exp=20*ratio*lvl
		self.tipe=tipe
	def lvlup(self):
		for att in range(len(self.attvalues)):
			self.attvalues[att]*=self.ratio*self.lvl
	def lvluptipe(self):
		if self.tipe == "warrior":
			self.attvalues=[20,20,3,1,1,0,0]
			self.lvlup()
				
		elif self.tipe == "guardian":
			self.attvalues=[30,10,2,3,1,0,2]
			self.lvlup()

		elif self.tipe == "assassin":
			self.attvalues=[10,30,6,0,3,0,0]
			self.lvlup()

		elif self.tipe == "mage":
			self.attvalues=[15,35,1,1,1,5,3]
			self.lvlup()

		elif self.tipe == "antimage":
			self.attvalues=[25,15,3,1,2,0,4]
			self.lvlup()

	def showatt(self):
		for att in range(len(self.attributes)):
			print self.attributes[att],self.attvalues[att]

#funcion para generar enemigos
def generateEnemy(ratio):
	ratio=ratio
	lvl=user.lvl
	random_tipe=random()
	print random_tipe
	if random_tipe<=0.2:
		random_tipe="warrior"
	elif random<=0.4:
		random_tipe="guardian"
	elif random<=0.6:
		random_tipe="assassin"
	elif random<=0.8:
		random_tipe="mage"
	else:
		random_tipe="antimage"
	print
	ene=enemy(ratio,lvl,random_tipe)
	ene.lvluptipe()
	return(ene)

user=champion("Alex","warrior")
#print user.name
#user.showatt()

enemy=generateEnemy(1.2)
print enemy.tipe
enemy.showatt()

print

if user.exp>=user.lvlexp:
	user.lvl+=1
	user.exp=0+(user.exp-user.lvlexp)
	user.lvluptipe()
	user.showatt()

#laberinto
marcador ="+"
x=1
y=19
px=1
py=19
mapa = open("laberinto.txt")
laberinto = mapa.readlines()
laberinto_lista=[]
laberinto_linea=[]
for linea in laberinto:
	for caracter in range(len(linea)):
		caracteres=linea[caracter]
		laberinto_linea.append(caracteres)

	laberinto_lista.append(laberinto_linea)
	laberinto_linea=[]

def movimiento(x,px,y,py):
	laberinto_lista[y][x]=" "
	laberinto_lista[py][px]=marcador
	conector=""
	laberinto_impreso=[]

	for linea in laberinto_lista:
		
		imprimir=conector.join(linea)
		
		laberinto_impreso.append(imprimir)
		
	laberinto_impreso=conector.join(laberinto_impreso)
	call(["clear"])
	print laberinto_impreso


exit = False
while exit == False:
	movimiento(x,px,y,py)
	move=getch.getch()
	if move == "a":
		px = x-1
		if laberinto_lista[py][px]=="|" or laberinto_lista[py][px]=="-":
			px = x
		else:
			movimiento(x,px,y,py)
			x = px
	elif move == "d":
		px = x+1
		if laberinto_lista[py][px]=="|" or laberinto_lista[py][px]=="-":
			px = x
		else:
			movimiento(x,px,y,py)
			x = px
	elif move == "w":
		py = y-1
		print laberinto[py][px]
		if laberinto_lista[py][px]=="|" or laberinto_lista[py][px]=="-":
			py = y
		else:
			movimiento(x,px,y,py)
			y = py
	elif move == "s":
		py = y+1
		print laberinto[py][px]
		if laberinto_lista[py][px]=="|" or laberinto_lista[py][px]=="-":
			py = y
		else:
			movimiento(x,px,y,py)
			y = py
	if py == 9 and px==10:
		print "Has ganado!"
		exit = True