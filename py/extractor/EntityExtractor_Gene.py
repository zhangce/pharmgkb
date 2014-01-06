#! /usr/bin/env python

import sys
import csv
csv.field_size_limit(sys.maxsize)

from extractor.Extractor import *
from dstruct.Gene import *
from dstruct.BinaryDependency import *

class EntityExtractor_Gene(Extractor):

	dict_gene_symbols = None

	def __init__(self):
		self.dict_gene_symbols = {}

	def loadDict(self):

		with open(BASE_FOLDER + "/dicts/genes.tsv") as tsv:
			r = csv.reader(tsv, dialect="excel-tab")
			headers = r.next()
			for line in r:
				#print line[4]
				self.dict_gene_symbols[line[4]] = line[3]

	def extract(self, doc):
		
		for sent in doc.sents:
			for word in sent.words:
				if word.word.upper() == word.word:
					if re.search(r"[A-Z]", word.word) and re.search(r"[0-9]", word.word):
						mention = GeneMention(word.word, [word,])
						doc.add_candidate_gene_mentions(sent.sentid, mention)

		for sentid in doc.candidate_gene_mentions:
			sent = doc.sents[sentid]
			for mention in doc.candidate_gene_mentions[sentid]:
				mention.add_features(sent.dep_parent(mention))

				for dep in sent.get_dependency_rightside(mention):
					doc.add_dependencies(BinaryDependency(dep[0], dep[1], dep[2]))

				for dep in sent.get_dependency_leftside(mention):
					doc.add_dependencies(BinaryDependency(dep[0], dep[1], dep[2]))

		negative_symbols = {}
		for sentid in doc.candidate_gene_mentions:
			sent = doc.sents[sentid]
			for mention in doc.candidate_gene_mentions[sentid]:
				if mention.symbol in self.dict_gene_symbols:
					mention.is_correct = True
				prev_word = sent.get_prev_wordobject(mention)
				if prev_word != None and prev_word.word in ['Figure', 'Table', 'individual']:
					mention.is_correct = False
					negative_symbols[mention.symbol] = 1

		for sentid in doc.candidate_gene_mentions:
			for mention in doc.candidate_gene_mentions[sentid]:
				if mention.symbol in negative_symbols:
					mention.is_correct = False

					









