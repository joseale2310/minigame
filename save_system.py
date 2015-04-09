#!/usr/bin/python
# -*- coding: utf-8 -*
from subprocess import call
from random import random
from characters import *
import cPickle as pickle
import os

def save(user):
	save_files=[]
	directories = os.listdir("./")
	for files in directories:
		if files[-5:] == ".file":
			save_files.append(files)

	print save_files
	file_chosen= raw_input("Choose where to save: ")
	with open(file_chosen, 'wb') as output:
		pickle.dump(user, output, -1)


def load():
	load_files=[]
	directories = os.listdir("./")
	for files in directories:
		if files[-5:] == ".file":
			load_files.append(files)

	print load_files
	file_chosen= raw_input("Choose file to load: ")
	with open(file_chosen, 'rb') as input:
		user = pickle.load(input)
		return(user)
