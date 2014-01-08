#! /usr/bin/env python

from helper.easierlife import *
from extractor.RelationExtractor_DrugGene import *

relation_drug_gene = RelationExtractor_DrugGene()
relation_drug_gene.loadDict()

for row in get_inputs():

	mention1 = deserialize(row["gene_mentions.m1"])
	mention2 = deserialize(row["gene_mentions.m2"])
	sentence = deserialize(row["sentences.sentence"])

	rel = RelationMention("DrugGene", mention1, mention2)
	rel.add_features([sentence.dep_path(mention1, mention2),])
	rel.is_correct = False
	print rel.dumps()
