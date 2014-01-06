#! /usr/bin/env python

from helper.easierlife import *

class Mention(object):

	id = None	
	type = None
	prov_words = None
	features = None

	is_correct = None

	def add_features(self, features):
		for f in features:
			self.features.append(f)

	def __init__(self, _type, _words):
		self.prov_words = []
		self.type = _type
		self.features = []
		for w in _words:
			self.prov_words.append(w)

	def __repr__(self):
		return "[" + self.type + " : " + myjoin(" ", self.prov_words, lambda w: w.word) + "]"