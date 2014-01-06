#! /usr/bin/env python

from dstruct.Entity import *

class DrugMention(Mention):
	name = None

	def __init__(self, _name, _words):

		super(DrugMention, self).__init__("DRUG", _words)
		self.name = _name