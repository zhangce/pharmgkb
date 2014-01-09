#! /usr/bin/env python

import codecs
from helper.easierlife import *

for doc in get_inputs():

	candidate_gene_mentions = deserialize(doc["documents.candidate_gene_mentions"])
	candidate_drug_mentions = deserialize(doc["documents.candidate_drug_mentions"])
	candidate_motabolite_mentions = deserialize(doc["documents.candidate_motabolite_mentions"])
	candidate_relation_mentions = deserialize(doc["documents.candidate_relation_mentions"])
	dependencies = deserialize(doc["documents.dependencies"])

	for dep in dependencies:
		print json.dumps({
			"mid1":dep.o1.id,
			"mid2":dep.o2.id,
			"feature":"[F-" + dep.o1.type + "-" + dep.o2.type + "] " + dep.feature
		})