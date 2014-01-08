#! /usr/bin/env python

from dstruct.Mention import *

class DrugMention(Mention):
	name = None

	def __init__(self, _docid, _name, _words):
		super(DrugMention, self).__init__(_docid, "DRUG", _words)
		self.name = _name