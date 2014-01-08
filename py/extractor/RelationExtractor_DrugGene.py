#! /usr/bin/env python

import sys
import csv
csv.field_size_limit(sys.maxsize)

from extractor.Extractor import *
from dstruct.Gene import *
from dstruct.BinaryDependency import *

from dstruct.Relation import *

class RelationExtractor_DrugGene(RelationExtractor):

	dict_drug_gene = None

	def __init__(self):
		self.dict_drug_gene = {}

	def loadDict(self):

		import os
		for f in os.listdir(BASE_FOLDER + "/dicts/pathways-tsv"):
			if f == '.DS_Store': continue
			with open(BASE_FOLDER + "/dicts/pathways-tsv/" + f) as tsv:
				r = csv.reader(tsv, dialect="excel-tab")
				headers = r.next()
				for line in r:
					for w in line[7].split(','):
						w = w.strip()
						if len(w) >= 3:
							if line[0].lower() not in self.dict_drug_gene:
								self.dict_drug_gene[line[0].lower()] = {}
							self.dict_drug_gene[line[0].lower()][w] = 1

	def extract(self, sent, mention1, mention2):

		rel = RelationMention("DrugGene", mention1, mention2)
		rel.add_features([sent.dep_path(mention1, mention2),])


		drug = mention1.name.lower()
		gene = mention2.symbol

		if drug in self.dict_drug_gene:
			if gene in self.dict_drug_gene[drug]:
				rel.is_correct = True

		rel.dumps()