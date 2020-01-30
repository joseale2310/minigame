#/usr/bin/env python
# -*- coding: utf-8 -*

#Import Modules
import os, pygame, sys
from glyph import Glyph
from pygame.locals import *
from mapprint_pygame import *
from main_menu import *
from pygame.font import Font


if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

user=main_menu()
map_loaded = map_load(user)
map_printed= map_print(user,map_loaded)
print (map_printed)
x = user.position[1]
y = user.position[2]
px = user.position[3]
py = user.position[4]
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Rolling in the Deep')
#pygame.mouse.set_visible(0)

#Create The Backgound
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))

#Put Text On The Background, Centered
if pygame.font:
	font = pygame.font.Font(None, 36)
	text = font.render("Rol test", 1, (0, 0, 0))
	textpos = text.get_rect(centerx=background.get_width()/2,centery=background.get_height()/2)
	background.blit(text, textpos)

screen.blit(background, (0, 0))
pygame.display.flip()

frames(map_printed,background,screen)


exit=False
clock = pygame.time.Clock()
while exit==False:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if  event.key  == K_d:
				
				px = x+1
				if map_loaded[py][px]=="|" or map_loaded[py][px]=="-":
					
					px = x

				else:
					
					map_printed = map_print(user,map_loaded)
					frames(map_printed,background,screen)
					print(map_printed)
					x = px
				
