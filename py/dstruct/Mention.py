#! /usr/bin/env python

from helper.easierlife import *

class Mention(object):

	docid = None
	sentid = None
	id = None	
	type = None
	prov_words = None
	features = None
	is_correct = None
	start_wid = None
	end_wid = None

	def add_features(self, features):
		for f in features:
			self.features.append(f)

	def __init__(self, _docid, _type, _words):
		self.docid = _docid
		self.prov_words = []
		self.type = _type
		self.features = []
		for w in _words:
			self.prov_words.append(w)
		self.sentid = _words[0].sentid
		self.start_wid = self.prov_words[0].insent_id
		self.end_wid = self.prov_words[-1].insent_id

	def dumps(self):
		return json.dumps({"docid":self.docid, "mid":self.id, "type":self.type, 
			"repr":self.__repr__(), "is_correct":self.is_correct,
			"features":self.features, "sentid":self.sentid, "start_wid":self.start_wid,
			"end_wid":self.end_wid, 
			"mid":"MENTION_%s_%s_SENT%d_%d_%d" % (self.type, self.docid, self.sentid, self.start_wid, self.end_wid),
			"object":serialize(self)})

	def __repr__(self):
		return "[" + self.type + " : " + " ".join([w.word for w in self.prov_words]) + "]"

