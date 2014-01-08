#! /usr/bin/env python

import codecs
from multiprocessing import *

from helper.easierlife import *

from dstruct.Document import *


"""
from extractor.EntityExtractor_Gene import *
from extractor.EntityExtractor_Drug import *
from extractor.RelationExtractor_DrugGene import *

INPUT_FOLDER = BASE_FOLDER + "/Pharm1K"

entity_gene = EntityExtractor_Gene()
entity_gene.loadDict()

entity_drug = EntityExtractor_Drug()
entity_drug.loadDict()

relation_drug_gene = RelationExtractor_DrugGene()
relation_drug_gene.loadDict()


	entity_gene.extract(doc)
	
	entity_drug.extract(doc)

	relation_drug_gene.extract(doc)

	fo = open(BASE_FOLDER + "/tmp/" + DOCID + ".json", 'w')
	doc.dump(fo)
	fo.close()
"""


for row in get_inputs():
	docid = row["docids.docid"]
	folder = row["docids.folder"]
	doc = Document(docid)
	doc.parse_doc(folder)
	print json.dumps({"docid":docid, "document":serialize(doc)})








