#!/usr/bin/python
# -*- coding: utf-8 -*
from subprocess import call
import getch
import cPickle as pickle
from random import random
from characters import *
from combat import *
from save_system import *

def menu(user):
	exit = False
	while exit == False:
		call(["clear"])
		user.showatt()
		action=getch.getch()
		if action == "s":
			save(user,"save.txt")
			print "Saving!"
			raw_input()

		elif action=="l":
			load(user,"save.txt")
			print "Loading!"
			raw_input()

		elif action == "p":
			exit= True
		 