#! /usr/bin/env python

import sys
import csv
csv.field_size_limit(sys.maxsize)

from extractor.Extractor import *
from dstruct.Gene import *
from dstruct.BinaryDependency import *

class EntityExtractor_Gene(MentionExtractor):

	dict_gene_symbols = None

	def __init__(self):
		self.dict_gene_symbols = {}

	def loadDict(self):

		with open(BASE_FOLDER + "/dicts/genes.tsv") as tsv:
			r = csv.reader(tsv, dialect="excel-tab")
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
		
		for sent in doc.sents:
			for word in sent.words:
				if word.word.upper() == word.word:
					if re.search(r"[A-Z]", word.word) and re.search(r"[0-9]", word.word):
						mention = GeneMention(doc.docid, word.word, [word,])
						mention.add_features(sent.dep_parent(mention))
						self.supervise(doc, sent, mention)
						print mention.dumps()




		"""

		for sentid in doc.candidate_gene_mentions:
			for mention in doc.candidate_gene_mentions[sentid]:
				if mention.symbol in negative_symbols:
					mention.is_correct = False
		"""		









