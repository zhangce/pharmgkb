#! /usr/bin/env python

import random
import sys
import csv

from extractor.Extractor import *
from dstruct.GeneMention import *

csv.field_size_limit(sys.maxsize)
GENE_DICT = "/dicts/genes.tsv"
DICT_DIALECT = "excel-tab"

class EntityExtractor_Gene(MentionExtractor):

	dict_gene_symbols = None

	def __init__(self):
		self.dict_gene_symbols = {}

	def loadDict(self):
		with open(BASE_FOLDER + GENE_DICT) as tsv:
			r = csv.reader(tsv, dialect=DICT_DIALECT)
			headers = r.next()
			for line in r:
				self.dict_gene_symbols[line[4]] = line[3]

	def supervise(self, doc, sent, mention):
		if mention.symbol in self.dict_gene_symbols:
			mention.is_correct = True
		prev_word = sent.get_prev_wordobject(mention)
		if prev_word != None and prev_word.word in ['Figure', 'Table', 'individual']:
			mention.is_correct = False

	def extract(self, doc):

		NEG_QUOTA = 100
		NEG_PROB = 0.1
		
		for sent in doc.sents:
			for word in sent.words:
				if word.word.upper() == word.word:
					if re.search(r"[A-Z]", word.word) and re.search(r"[0-9]", word.word):
						mention = GeneMention(doc.docid, word.word, [word,])
						mention.add_features(sent.dep_parent(mention))
						self.supervise(doc, sent, mention)
						print mention.dumps()
				elif NEG_QUOTA > 0 and random.random() < NEG_PROB:
					negative_mention = GeneMention(doc.docid, word.word, [word,])
					negative_mention.add_features(sent.dep_parent(negative_mention))
					negative_mention.is_correct = False
					NEG_QUOTA = NEG_QUOTA - 1
					print negative_mention.dumps()



