#!/usr/bin/python
# -*- coding: utf-8 -*
from subprocess import call
import getch, os
import cPickle as pickle
import pygame
from random import random
from random import uniform
from characters import *
from combat import *
from save_system import *
from pause_menu import *
from main_menu import *

user = main_menu()
pygame.mixer.init()
sound=pygame.mixer.Sound("../sounds/prueba.wav")
sound.play(loops=-1)
#maps
marcador ="+"
x = user.position[1]
y = user.position[2]
px = user.position[3]
py = user.position[4]
mapa = open(user.position[0])
maps = mapa.readlines()
maps_lista=[]
maps_linea=[]
for linea in maps:
	for caracter in range(len(linea)):
		caracteres=linea[caracter]
		maps_linea.append(caracteres)

	maps_lista.append(maps_linea)
	maps_linea=[]

def movimiento(x,px,y,py):
	maps_lista[y][x] = " "
	maps_lista[py][px] = marcador
	conector = ""
	maps_impreso = []

	for linea in maps_lista:
		
		imprimir=conector.join(linea)
		
		maps_impreso.append(imprimir)
		
	maps_impreso=conector.join(maps_impreso)
	call(["clear"])
	print maps_impreso

exit = False
while exit == False:

	movimiento(x,px,y,py)
	move=getch.getch()
	if move == "a":
		px = x-1
		if maps_lista[py][px] == "|" or maps_lista[py][px]=="-":
			px = x
		elif maps_lista[py][px] == "#":
			result=combate(user)
			if result == True:
				movimiento(x,px,y,py)
				x = px
			else:
				px = x
		else:
			movimiento(x,px,y,py)
			x = px
	elif move == "d":
		px = x+1
		if maps_lista[py][px]=="|" or maps_lista[py][px]=="-":
			px = x
		elif maps_lista[py][px]=="#":
			result=combate(user)
			if result == True:
				movimiento(x,px,y,py)
				x = px
			else:
				px = x	
		else:
			movimiento(x,px,y,py)
			x = px
	elif move == "w":
		py = y-1
		print maps[py][px]
		if maps_lista[py][px]=="|" or maps_lista[py][px]=="-":
			py = y
		elif maps_lista[py][px]=="#":
			result=combate(user)
			if result == True:
				movimiento(x,px,y,py)
				y = py
			else:
				py = y	
		else:
			movimiento(x,px,y,py)
			y = py
	elif move == "s":
		py = y+1
		print maps[py][px]
		if maps_lista[py][px]=="|" or maps_lista[py][px]=="-":
			py = y
		elif maps_lista[py][px]=="#":
			result=combate(user)
			if result == True:
				movimiento(x,px,y,py)
				y = py
			else:
				py = y
		else:
			movimiento(x,px,y,py)
			y = py

	elif move == "p":
		user.position = ["laberinto.txt",x,y,px,py]
		exit = menu(user)

	if py == 9 and px ==10:
		print "You have won the game!"
		exit = True


