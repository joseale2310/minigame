#!/usr/bin/python
# -*- coding: utf-8 -*
from subprocess import call
from random import random
from random import uniform
from characters import *
#########################################################################################
def generateEnemy(ratio,lvl):
	"""Function in order to generate enemies in a random way"""
	ratio = ratio
	random_tipe = random()
	
	if random_tipe <= 0.2:
		random_tipe = "warrior"
	elif random_tipe <= 0.4:
		random_tipe="guardian"
	elif random_tipe <= 0.6:
		random_tipe = "assassin"
	elif random_tipe <= 0.8:
		random_tipe = "mage"
	elif random_tipe <= 1:
		random_tipe = "antimage"

	ene = enemy(ratio,lvl,random_tipe)
	ene.lvluptipe()
	return(ene)

def userattacks(user,enemy,totalDamageDone):
	print "Your turn!"
	raw_input()
	damageDone = round(user.attvalues[2]*uniform(user.attvalues[7],1)*(1-(enemy.attvalues[3]/100)),2)
	print "You have done",damageDone,"damage points!"
	totalDamageDone += damageDone
	raw_input()
	return(totalDamageDone)

def enemyattacks(user,enemy,damageRecived):
	print "Your enemy attacks!"
	raw_input()
	damageDone = round(enemy.attvalues[2]*uniform(enemy.attvalues[7],1)*(1-(user.attvalues[3]/100)),2)
	damageRecived += damageDone
	print "You have recived",damageDone,"damage points!.","You have",(user.attvalues[0]-damageRecived), "HP left!"
	raw_input()
	return(damageRecived)

#combate
def combate(user):
	"""Function to make fights"""
	call(["clear"])
	turn_value = 100
	enemy_turn = 0
	user_turn = 0
	damageDone = 0
	totalDamageDone = 0
	damageRecived = 0
	fight = False
	win = False 
	enemy=generateEnemy(1+random(),user.lvl)
	print "You have entered in combat with a " + enemy.tipe + "!\n"

	while fight == False:
		if totalDamageDone >= enemy.attvalues[0]:
			raw_input()
			print "You have defeated the " + enemy.tipe + "!"
			print "You have earned",enemy.exp,"exp points!"
			user.exp += enemy.exp
			user.checklvl()
			raw_input() 
			win = True
			fight = True

		elif damageRecived >= user.attvalues[0]:
			print "You are dead!"
			raw_input()
			win = False
			fight = True
		else:
			user_turn+=user.attvalues[4]
			enemy_turn+=enemy.attvalues[4]
			
			if user_turn >= turn_value and enemy_turn >= turn_value:
				
				if user_turn > enemy_turn:
					totalDamageDone = userattacks(user,enemy,totalDamageDone)
					damageRecived = enemyattacks(user,enemy,damageRecived)
					user_turn -= turn_value	
					enemy_turn -= turn_value

				elif user_turn == enemy_turn:
					user_random = random()
					enemy_random = random()
					if user_random > enemy_random:
						totalDamageDone = userattacks(user,enemy,totalDamageDone)
						damageRecived = enemyattacks(user,enemy,damageRecived)
						user_turn -= turn_value	
						enemy_turn -= turn_value
					else:
						damageRecived = enemyattacks(user,enemy,damageRecived)
			 			totalDamageDone = userattacks(user,enemy,totalDamageDone)
			 			user_turn -= turn_value	
						enemy_turn -= turn_value

			 	else:
			 		damageRecived = enemyattacks(user,enemy,damageRecived)
			 		totalDamageDone = userattacks(user,enemy,totalDamageDone)
			 		user_turn -= turn_value	
					enemy_turn -= turn_value

			elif user_turn >= turn_value and enemy_turn < turn_value:
				totalDamageDone = userattacks(user,enemy,totalDamageDone)
				user_turn -= turn_value	

			elif user_turn < turn_value and enemy_turn >= turn_value:
				damageRecived = enemyattacks(user,enemy,damageRecived)
				enemy_turn -= turn_value				

	return(win)