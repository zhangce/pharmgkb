#! /usr/bin/env python

import fileinput
import json
import math
import zlib
import sys
import os
import cPickle as pickle
import itertools
import os

BASE_FOLDER, throwaway = os.path.split(os.path.realpath(__file__))
BASE_FOLDER = BASE_FOLDER + "/../../"


def get_all_phrases_in_sentence(sent, max_phrase_length):
	for start in range(0, len(sent.words)):
		for end in reversed(range(start + 1, min(len(sent.words), start + 1 + max_phrase_length))):
			yield (start, end)
		



def log(str):
	sys.stderr.write(str.__repr__() + "\n")

def serialize(obj):
	#return zlib.compress(pickle.dumps(obj))
	return pickle.dumps(obj)

def deserialize(obj):
	#return pickle.loads(str(unicode(obj)))
	return pickle.loads(obj.encode("utf-8"))

def get_inputs():
	for line in fileinput.input():
		#line = line.rstrip()
		yield json.loads(line)
		#try:
		#	yield json.loads(line)
		#except:
		#	log("ERROR!  :  " + line)

def dump_input(OUTFILE):
	fo = open(OUTFILE, 'w')
	for line in fileinput.input():
		fo.write(line)
	fo.close()







