#/usr/bin/env python
# -*- coding: utf-8 -*
import pygame, os
from pygame.locals import *
from glyph import Glyph
from pygame.font import Font

if not pygame.font: print 'Warning, fonts disabled'

def map_load(user):
	mapa = open(user.position[0])
	maps = mapa.readlines()
	maps_lista=[]
	maps_linea=[]
	for linea in maps:
		linea=linea.rstrip('\n') + "/n"
		print linea
		for caracter in range(len(linea)):
			caracteres=linea[caracter]
			maps_linea.append(caracteres)

		maps_lista.append(maps_linea)
		maps_linea=[]
	return (maps_lista)

def map_print(user,maps):
	FONT = Font("silkscreen.ttf",16)
	DEFAULT = {
    'bkg'       : (0, 0, 0),
    'color'     : (250, 250, 250),
    'font'      : FONT,
    'spacing'   : 0, #FONT.get_linesize(),
    }
	x = user.position[1]
	y = user.position[2]
	px = user.position[3]
	py = user.position[4]
	maps[y][x] = " "
	maps[py][px] = "+"
	conector = ""
	maps_impreso = []

	for linea in maps:
		
		imprimir=conector.join(linea)
		
		maps_impreso.append(imprimir)
		
	maps_impreso=conector.join(maps_impreso)
	glyph=Glyph(Rect(0,0,600,600),ncols=1,**DEFAULT)
	glyph.input(maps_impreso, justify = 'justified')
	glyph.update()
    
	return(glyph)

def frames(maps,background,screen):
	maps_rect = maps.rect
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((0, 0, 0))
	screen.blit(background, (0, 0))
	screen.blit(maps.image, maps_rect)
	pygame.display.flip()