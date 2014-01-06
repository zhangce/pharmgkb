#! /usr/bin/env python

from helper.easierlife import *

class RelationMention(object):

	id = None	
	type = None

	m1 = None
	m2 = None

	features = None

	is_correct = None

	def add_features(self, features):
		for f in features:
			self.features.append(f)

	def __init__(self, _type, _m1, _m2):
		self.type = _type
		self.features = []
		self.m1 = _m1
		self.m2 = _m2

	def __repr__(self):
		return "[" + self.type + " : " + self.m1.__repr__() + " | " + self.m2.__repr__() + "]"