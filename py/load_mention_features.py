#! /usr/bin/env python

import codecs
from helper.easierlife import *

for doc in get_inputs():

	candidate_gene_mentions = deserialize(doc["documents.candidate_gene_mentions"])
	candidate_drug_mentions = deserialize(doc["documents.candidate_drug_mentions"])
	candidate_motabolite_mentions = deserialize(doc["documents.candidate_motabolite_mentions"])
	candidate_relation_mentions = deserialize(doc["documents.candidate_relation_mentions"])
	dependencies = deserialize(doc["documents.dependencies"])

	dicts = [candidate_gene_mentions, candidate_drug_mentions, candidate_motabolite_mentions]
	for d in dicts:
		for sentid in d:
			for mention in d[sentid]:
				for feature in mention.features:
					print json.dumps({
						"mid":mention.id, 
						"feature":"[F-" + mention.type + "] " + feature
					})