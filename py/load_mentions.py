#! /usr/bin/env python

import codecs
from multiprocessing import *

from helper.easierlife import *

"""
psql -U $DB_USER -c "CREATE TABLE mentions (id   bigserial primary key, \
											mid          text,                  \
											type         text,                   \
											is_correct   text,                   \
											repr         text);"					$DB_NAME

"""

for doc in get_inputs():

	candidate_gene_mentions = deserialize(doc["documents.candidate_gene_mentions"])
	candidate_drug_mentions = deserialize(doc["documents.candidate_drug_mentions"])
	candidate_motabolite_mentions = deserialize(doc["documents.candidate_motabolite_mentions"])
	candidate_relation_mentions = deserialize(doc["documents.candidate_relation_mentions"])
	dependencies = deserialize(doc["documents.dependencies"])

	dicts = [candidate_gene_mentions, candidate_drug_mentions, candidate_motabolite_mentions]
	for d in dicts:
		for sentid in d:
			for m in d[sentid]:
				print json.dumps({"mid":m.id, "type":m.type, "repr":m.__repr__(), "is_correct":m.is_correct})
				