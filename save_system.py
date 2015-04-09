#!/usr/bin/python
# -*- coding: utf-8 -*
from subprocess import call
from random import random
from characters import *
import cPickle as pickle

def save(user,save_file):
	with open(save_file, 'wb') as output:
    pickle.dump(user, output, -1)


def load(user,save_file):
	with open('save_file', 'rb') as input:
    user = pickle.load(input)
