# -*- coding: utf-8 -*
from subprocess import call
import getch
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
	print (laberinto_impreso)


print ("hola!")
print ("Estas aquí",py,px)
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
		print (laberinto[py][px])
		if laberinto_lista[py][px]=="|" or laberinto_lista[py][px]=="-":
			py = y
		else:
			movimiento(x,px,y,py)
			y = py
	elif move == "s":
		py = y+1
		print (laberinto[py][px])
		if laberinto_lista[py][px]=="|" or laberinto_lista[py][px]=="-":
			py = y
		else:
			movimiento(x,px,y,py)
			y = py
	if py == 9 and px==10:
		print ("Has ganado!")
		exit = True
