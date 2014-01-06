#! /usr/bin/env python

import codecs
from multiprocessing import *

from helper.easierlife import *

from dstruct.Document import *

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

class Task:
	docid = None
	def __init__(self): 
		self.docid = ""


def process(task):

	global INPUT_FOLDER

	DOCID = task.docid

	DOCDIR = INPUT_FOLDER

	doc = Document(DOCID)

	doc.parse_doc(DOCDIR + "/" + DOCID)

	entity_gene.extract(doc)
	
	entity_drug.extract(doc)

	relation_drug_gene.extract(doc)

	fo = open(BASE_FOLDER + "/tmp/" + DOCID + ".json", 'w')
	doc.dump(fo)
	fo.close()

	

log("START LOADING DOCUMENTS!")

def do():
	tasks = []
	for docid in os.listdir(INPUT_FOLDER):
		if docid.startswith('.'): continue

		task = Task()
		task.docid = docid
		tasks.append(task)

	#ct = 0
	#for task in tasks:
	#	ct = ct + 1
	#	process(task)
	#
	#	log(ct)
	#	if ct > 100:
	#		break

	pool = Pool(8)
	pool.map(process, tasks)

do()

#import cProfile
#cProfile.run('do()')








