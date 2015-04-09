#!/usr/bin/python
# -*- coding: utf-8 -*
from subprocess import call
import getch
import cPickle as pickle
from random import random
from characters import *
from combat import *
from save_system import *
from menu import *

call(["clear"])

main_menu = True

while main_menu:
	print "1. Start new adventure"
	print "2. Load adventure"
	option = raw_input("1/2: ")
	
	if option == "1":
		print "\n"
		user = createuser()
		raw_input()
		main_menu =False

	elif option == "2":
		print "\n"
		user = load("save.txt")
		main_menu = False
