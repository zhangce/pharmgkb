#! /usr/bin/env pypy

from helper.easierlife import *
from extractor.EntityExtractor_Drug import *

for row in get_inputs():
	doc = deserialize(row["documents.document"])
	log(doc.docid)
	for sent in doc.sents:
		print json.dumps({
			"docid": doc.docid, 
			"sentid":sent.sentid, 
			"sentence": serialize(sent)
    })

