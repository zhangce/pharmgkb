#! /usr/bin/env python

import sys
import csv
csv.field_size_limit(sys.maxsize)

from extractor.Extractor import *
from dstruct.Drug import *
from dstruct.BinaryDependency import *

class EntityExtractor_Drug(MentionExtractor):

	dict_drug_names = None
	dict_english    = None

	def __init__(self):
		self.dict_drug_names = {}
		self.dict_english = {}

	def loadDict(self):

		with open(BASE_FOLDER + "/dicts/drugs.tsv") as tsv:
			r = csv.reader(tsv, dialect="excel-tab")
			headers = r.next()
			for line in r:
				#print line[1]
				self.dict_drug_names[line[1].lower()] = line[1]
				for w in line[2].split(","):
					if len(w) > 5:
						self.dict_drug_names[w.lower()] = line[1]
				for w in line[3].split(","):
					if len(w) > 5:
						self.dict_drug_names[w.lower()] = line[1]


		with open(BASE_FOLDER + "/dicts/FDA_Approved_Drugs.txt") as tsv:
			r = csv.reader(tsv, dialect="excel-tab")
			headers = r.next()
			for line in r:
				self.dict_drug_names[line[7].lower()] = line[7]

		for l in open(BASE_FOLDER + "/dicts/words"):
			self.dict_english[l.rstrip().lower()] = 1


	def supervise(self, doc, mention):
		if mention.name in self.dict_drug_names and mention.name not in self.dict_english:
			mention.is_correct = True
		if mention.name in self.dict_drug_names and mention.name in self.dict_english:
			mention.is_correct = False

	def extract(self, doc):

		for sent in doc.sents:
			for (start, end) in get_all_phrases_in_sentence(sent, 5):

				phrase = myjoin(" ", sent.words[start:end], lambda (w) : w.word)
				ner = myjoin(" ", sent.words[start:end], lambda (w) : w.ner)
				lemma = myjoin(" ", sent.words[start:end], lambda (w) : w.lemma)

				if lemma.lower() in self.dict_drug_names:
					mention = DrugMention(doc.docid, lemma.lower(), sent.words[start:end])
					mention.add_features(sent.dep_parent(mention))
					self.supervise(doc, mention)
					print mention.dumps()





