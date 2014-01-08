#! /usr/bin/env python

import random
import sys
import csv
csv.field_size_limit(sys.maxsize)

from extractor.Extractor import *
from dstruct.Drug import *

DRUG_DICT = "/dicts/drugs.tsv"
DICT_DIALECT = "excel-tab"

class EntityExtractor_Drug(MentionExtractor):

	dict_drug_names = None
	dict_english    = None

	def __init__(self):
		self.dict_drug_names = {}
		self.dict_english = {}

	def loadDict(self):

		with open(BASE_FOLDER + DRUG_DICT) as tsv:
			r = csv.reader(tsv, dialect=DICT_DIALECT)
			headers = r.next()
			for line in r:
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
		#if mention.name in self.dict_drug_names and mention.name in self.dict_english:
		#	mention.is_correct = False

	def extract(self, doc):

		NEG_QUOTA = 100
		NEG_PROB = 0.01

		for sent in doc.sents:
			for (start, end) in get_all_phrases_in_sentence(sent, 5):

				phrase = " ".join([w.word for w in sent.words[start:end]])
				ner = " ".join([w.ner for w in sent.words[start:end]])
				lemma = " ".join([w.lemma for w in sent.words[start:end]])

				if lemma.lower() in self.dict_drug_names:
					mention = DrugMention(doc.docid, lemma.lower(), sent.words[start:end])
					mention.add_features(sent.dep_parent(mention))
					self.supervise(doc, mention)
					print mention.dumps()

				elif NEG_QUOTA > 0 and random.random() < NEG_PROB:
					negative_mention = DrugMention(doc.docid, lemma.lower(), sent.words[start:end])
					negative_mention.add_features(sent.dep_parent(negative_mention))
					negative_mention.is_correct = False
					NEG_QUOTA = NEG_QUOTA - 1
					print negative_mention.dumps()







