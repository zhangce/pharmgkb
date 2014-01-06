#! /usr/bin/env python

import sys
import csv
csv.field_size_limit(sys.maxsize)

from extractor.Extractor import *
from dstruct.Gene import *
from dstruct.BinaryDependency import *

from dstruct.Relation import *

class RelationExtractor_DrugGene(Extractor):

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

	def extract(self, doc):

		NEG_QUOTA = 100

		for sentid in doc.candidate_drug_mentions:
			if sentid not in doc.candidate_gene_mentions: continue
			sent = doc.sents[sentid]

			for drug_mention in doc.candidate_drug_mentions[sentid]:
				for gene_mention in doc.candidate_gene_mentions[sentid]:

					rel = RelationMention("DrugGene", drug_mention, gene_mention)
					rel.add_features([sent.dep_path(drug_mention, gene_mention),])

					doc.add_candidate_relation_mentions(sentid, rel)


				for drug_mention2 in doc.candidate_drug_mentions[sentid]:
					if drug_mention2 != drug_mention and NEG_QUOTA > 50:

						NEG_QUOTA = NEG_QUOTA - 1

						rel = RelationMention("DrugGene", drug_mention, drug_mention2)
						rel.add_features([sent.dep_path(drug_mention, drug_mention2),])

						doc.add_candidate_relation_mentions(sentid, rel)

		for sentid in doc.candidate_gene_mentions:
			sent = doc.sents[sentid]
			for drug_mention in doc.candidate_gene_mentions[sentid]:
				for drug_mention2 in doc.candidate_gene_mentions[sentid]:
					if drug_mention2 != drug_mention and NEG_QUOTA > 0:

						NEG_QUOTA = NEG_QUOTA - 1
						rel = RelationMention("DrugGene", drug_mention, drug_mention2)
						rel.add_features([sent.dep_path(drug_mention, drug_mention2),])

						doc.add_candidate_relation_mentions(sentid, rel)


		for sentid in doc.candidate_relation_mentions:
			for relation in doc.candidate_relation_mentions[sentid]:

				if relation.m2.type == 'GENE' and relation.m1.type == 'DRUG':

					drug = relation.m1.name.lower()
					gene = relation.m2.symbol

					if drug in self.dict_drug_gene:
						if gene in self.dict_drug_gene[drug]:
							#log("++++")
							relation.is_correct = True

				else:
					#log("----")
					relation.is_correct = False













