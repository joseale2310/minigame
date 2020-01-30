# -*- coding: utf-8 -*
from subprocess import call
import getch
import pickle
from random import random
from random import uniform
from characters import *
from combat import *
from save_system import *

def menu(user):
	exit = False
	resume = False
	while resume == False:
		call(["clear"])
		print ("Pause menu\n")
		options = "S: save  L: load  P: resume  E: exit game\n"
		print (options + "-"*len(options)+"\n")
		title=user.name+" attributes\n"
		print (title+"-"*len(title))
		user.showatt()
		action=getch.getch()
		if action == "s":
			save(user)
			input()

		elif action=="l":
			user = load()
			print ("Loading!")
			input()

		elif action == "p":
			exit = False
			resume = True
			return(exit)

		elif action == "e":
			sure = input("\nAre you sure you want to leave? 1.Yes or 2.No: ")
			if sure == "1":
				exit = True
				resume = True
				return(exit)
			elif sure == "2":
				exit = False
			

