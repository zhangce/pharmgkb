#! /usr/bin/env python

from helper.easierlife import *
import codecs

import os
for f in os.listdir(BASE_FOLDER + "/tmp/"):
	if f.endswith('.json'):
		for l in open(BASE_FOLDER + "/tmp/" + f):
			try:
				aa = json.loads(l)
				rs = {}
				rs["docid"] = aa["docid"]
				rs["candidate_gene_mentions"] = aa["candidate_gene_mentions"]
				rs["candidate_drug_mentions"] = aa["candidate_drug_mentions"]
				rs["candidate_motabolite_mentions"] = aa["candidate_motabolite_mentions"]
				rs["candidate_relation_mentions"] = aa["candidate_relation_mentions"]
				rs["dependencies"] = aa["dependencies"]
				print json.dumps(rs)
			except:
				continue
