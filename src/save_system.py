#!/usr/bin/python
# -*- coding: utf-8 -*
from subprocess import call
from random import random
from random import uniform
from characters import *
import cPickle as pickle
import os

def save(user):
	i=0
	string=""
	save_files=[]
	directories = os.listdir("./")
	for files in directories:
		if files[-5:] == ".file":
			i+=1
			string += str(i)+". "+files[:-5]+" " 
			save_files.append(files)
	print "\n"+string+"0. Create new save.file  Q. Cancel"
	success = False
	while success == False:
		file_chosen = input("Choose saving file: ")

		if file_chosen=="0":
			save_name = input("Saving file name: ")
			if save_name.lower() == "q":
				print "Cancel"
				success = True 
			else:
				save_name +=".file"
				with open(save_name, 'wb') as output:
					pickle.dump(user, output, -1)
				print "Saving!"
				success = True

		elif file_chosen.lower()=="q":
			print "Cancel"
			success = True
			
		elif file_chosen.isdigit():
			if int(file_chosen) in range(1,len(save_files)+1):	
				with open(save_files[int(file_chosen)-1], 'wb') as output:
					pickle.dump(user, output, -1)
				print "\nSaving!"
				success = True
		else:
			print "There isn't that option\n"
			success = True

def load():
	i=0
	string=""
	load_files=[]
	directories = os.listdir("./")
	for files in directories:
		if files[-5:] == ".file":
			i+=1
			string += str(i)+". "+files[:-5]+" " 
			load_files.append(files)

	print "\n" + string
	success = False
	while success == False:
		file_chosen = input("Choose file to load or enter 'Q' to cancel: ")
		
		if file_chosen.isdigit():
			if int(file_chosen) in range(1,len(load_files)+1): 
				with open(load_files[int(file_chosen)-1], 'rb') as input:
					user = pickle.load(input)
				return(user)

		elif file_chosen.lower()=="q":
				print "Cancel"
				user = False
				return(user)
				success = True
