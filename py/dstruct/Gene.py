#! /usr/bin/env python


from dstruct.Entity import *

class GeneMention(Mention):
	symbol = None

	def __init__(self, _symbol, _words):

		super(GeneMention, self).__init__("GENE", _words)
		self.symbol = _symbol