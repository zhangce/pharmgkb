#! /usr/bin/env python

import codecs
from multiprocessing import *

from helper.easierlife import *

from extractor.RelationExtractor_DrugGene import *

relation_drug_gene = RelationExtractor_DrugGene()
relation_drug_gene.loadDict()

"""
input: "SELECT t0.docid, t0.document, array_agg(t1.object) from documents t0, 
mentions t1 WHERE t0.docid=t1.docid GROUP BY t0.docid, t0.document;"
"""
for row in get_inputs():

	mention1 = deserialize(row["mentions.m1"])
	mention2 = deserialize(row["mentions.m2"])
	sentence = deserialize(row["sentences.sentence"])

	relation_drug_gene.extract(sentence, mention1, mention2)
