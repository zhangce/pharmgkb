#! /usr/bin/env python

class BinaryDependency(object):

	o1 = None
	o2 = None
	feature = None

	def __init__(self, o1, o2, feature):
		self.o1 = o1
		self.o2 = o2
		self.feature = feature
