#!/usr/bin/python
# -*- coding: utf-8 -*
from subprocess import call
from random import random
from characters import *
#########################################################################################
def generateEnemy(ratio,lvl):
	"""Function in order to generate enemies in a random way"""
	ratio = ratio
	random_tipe = random()
	
	if random_tipe <= 0.2:
		random_tipe = "warrior"
	elif random <= 0.4:
		random_tipe="guardian"
	elif random <= 0.6:
		random_tipe = "assassin"
	elif random <= 0.8:
		random_tipe = "mage"
	else:
		random_tipe = "antimage"

	ene = enemy(ratio,lvl,random_tipe)
	ene.lvluptipe()
	return(ene)

#combate
def combate(user):
	"""Function to make fights"""
	call(["clear"])
	damageDone = 0
	totalDamageDone = 0
	damageRecived = 0
	fight = False
	win = False 
	enemy=generateEnemy(1.2,user.lvl)
	print "You have entered in combat with a " + enemy.tipe + "!"

	while fight == False:
		if totalDamageDone >= enemy.attvalues[0]:
			print "You have defeated the " + enemy.tipe + "!"
			print "You have earned",enemy.exp,"exp points!"
			user.exp += enemy.exp
			user.checklvl()
			raw_input() 
			win = True
			fight = True

		elif damageRecived >= user.attvalues[0]:
			print "You are dead!"
			win = False
			fight = True
		else:
			if user.attvalues[4]>enemy.attvalues[4]:
				print "Your turn!"
				raw_input()
				damageDone = round(user.attvalues[2]*(1-(enemy.attvalues[3]/(100+enemy.attvalues[3]))),2)
				print "You have done",damageDone,"damage points!"
				totalDamageDone += damageDone
				
				print "Your enemy attacks!"
				damageDone += round(enemy.attvalues[2]*(1-(user.attvalues[3]/(100+user.attvalues[3]))),2)
				damageRecived += damageDone
				print "You have recived",damageDone,"damage points!.","You have",(user.attvalues[0]-damageRecived), "health points left!"
				
			else:
				print "El enemigo ataca!"
				damageDone = round(enemy.attvalues[2]*(1-(user.attvalues[3]/(100+user.attvalues[3]))),2)
				damageRecived += damageDone
				print "You have recived",damageDone,"damage points!.","You have",(user.attvalues[0]-damageRecived), "health points left!"
				
				print "Tu turno!"
				raw_input()
				damageDone = round(user.attvalues[2]*(1-(enemy.attvalues[3]/(100+enemy.attvalues[3]))),2)
				print "You have done",damageDone,"damage points!"
				totalDamageDone += damageDone
				

	return(win)