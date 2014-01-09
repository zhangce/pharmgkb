#! /usr/bin/env python

import sys
import csv
import os
from extractor.Extractor import *
from dstruct.GeneMention import *
from dstruct.Relation import *

DICT_PATHWAY="/dicts/pathways-tsv/"
DICT_DIALECT="excel-tab"
csv.field_size_limit(sys.maxsize)

class RelationExtractor_DrugGene(RelationExtractor):

	dict_drug_gene = None

	def __init__(self):
		self.dict_drug_gene = {}

	def loadDict(self):
		for f in os.listdir(BASE_FOLDER + DICT_PATHWAY):
			if f == '.DS_Store': continue
			with open(BASE_FOLDER + DICT_PATHWAY + f) as tsv:
				r = csv.reader(tsv, dialect=DICT_DIALECT)
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

		if (drug in self.dict_drug_gene) and (gene in self.dict_drug_gene[drug]):
			rel.is_correct = True

		return rel