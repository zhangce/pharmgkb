#! /usr/bin/env python

from helper.easierlife import *
from extractor.EntityExtractor_Gene import *

entity_gene = EntityExtractor_Gene()
entity_gene.loadDict()

for row in get_inputs():
	doc = deserialize(row["documents.document"])
	entity_gene.extract(doc)			