#!/usr/bin/python
# -*- coding: utf-8 -*
from subprocess import call
import pygame, os
from pygame.locals import *
from random import random, uniform
import cPickle as pickle
from characters import *
from combat import *
from save_system import *
from pause_menu import *
from main_menu import *

user = main_menu()
pygame.init()
clock = pygame.time.Clock()
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
	clock.tick(60)
	movimiento(x,px,y,py)
	for event in pygame.event.get():
		if event.type == QUIT:
			exit = True
		elif event.type == KEYDOWN and event.key == K_a:
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
		elif event.type == KEYDOWN and event.key  == K_d:
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
		elif event.type == KEYDOWN and event.key  == K_w:
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
		elif event.type == KEYDOWN and event.key  == K_s:
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

		elif event.type == KEYDOWN and event.key  == K_p:
			user.position = ["laberinto.txt",x,y,px,py]
			exit = menu(user)

		if py == 9 and px ==10:
			print "You have won the game!"
			exit = True


