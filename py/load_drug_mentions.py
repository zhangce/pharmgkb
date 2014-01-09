#! /usr/bin/env pypy

from helper.easierlife import *
from extractor.EntityExtractor_Drug import *

entity_drug = EntityExtractor_Drug()
entity_drug.loadDict()

for row in get_inputs():
	doc = deserialize(row["documents.document"])
	for drug in entity_drug.extract(doc):
		if drug != None:
			print drug.dumps()