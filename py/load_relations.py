#! /usr/bin/env python

import codecs
from multiprocessing import *

from helper.easierlife import *

"""
psql -U $DB_USER -c "CREATE TABLE relations (id   bigserial primary key, \
											type             text,
											gene_id          text,                  \
											drug_id          text,                \
											is_correct       boolean);"					$DB_NAME
"""

for doc in get_inputs():

	candidate_gene_mentions = deserialize(doc["documents.candidate_gene_mentions"])
	candidate_drug_mentions = deserialize(doc["documents.candidate_drug_mentions"])
	candidate_motabolite_mentions = deserialize(doc["documents.candidate_motabolite_mentions"])
	candidate_relation_mentions = deserialize(doc["documents.candidate_relation_mentions"])
	dependencies = deserialize(doc["documents.dependencies"])

	dicts = [candidate_relation_mentions,]
	for d in dicts:
		for sentid in d:
			for m in d[sentid]:
				print json.dumps({"drug_id":m.m1.id, "type":m.type, "gene_id":m.m2.id, "is_correct":m.is_correct})
				