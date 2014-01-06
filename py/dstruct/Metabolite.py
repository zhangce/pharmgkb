#! /usr/bin/env python

from dstruct.Entity import *

class MetaboliteMention(Mention):
	name = None

	def __init__(self, _name, _words):

		super(MetaboliteMention, self).__init__("METABOLITE", _words)
		self.name = _name