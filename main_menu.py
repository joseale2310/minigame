#!/usr/bin/python
# -*- coding: utf-8 -*
from subprocess import call
import getch
import cPickle as pickle
from random import random
from characters import *
from combat import *
from save_system import *

def main_menu():
	main_menu = True
	while main_menu:
		call(["clear"])
		print "1. Start new adventure"
		print "2. Load adventure"
		option = raw_input("Enter option 1 or 2: ")
		
		if option == "1":
			print "\n"
			user = createuser()
			raw_input()
			main_menu = False
			return(user)

		elif option == "2":
			print "\n"
			user = load()
			if user != False:
				main_menu = False
				return(user)
