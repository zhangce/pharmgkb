#! /usr/bin/env python

import codecs
from multiprocessing import *

from helper.easierlife import *

from extractor.EntityExtractor_Drug import *

entity_drug = EntityExtractor_Drug()

entity_drug.loadDict()

for row in get_inputs():
	doc = deserialize(row["documents.document"])
	for sent in doc.sents:
		print json.dumps({"docid":doc.docid, "sentid":sent.sentid, "sentence": serialize(sent)})

