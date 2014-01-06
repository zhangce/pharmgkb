#! /usr/bin/env python

import codecs
from multiprocessing import *

from helper.easierlife import *

"""
psql -U $DB_USER -c "CREATE TABLE mentions_features (id   bigserial primary key, \
											mid          text,                  \
											feature      text);"					$DB_NAME

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
				for feature in m.features:
					print json.dumps({"mid":m.id, "feature":"[F-" + m.type + "] " + feature})