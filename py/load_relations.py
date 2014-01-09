#! /usr/bin/env python

from helper.easierlife import *
from extractor.RelationExtractor_DrugGene import *

# Initialize the extractor
relation_drug_gene = RelationExtractor_DrugGene()
relation_drug_gene.loadDict()

for row in get_inputs():
	
  mention1 = deserialize(row["drug_mentions.m1"])
  mention2 = deserialize(row["gene_mentions.m2"])
  sentence = deserialize(row["sentences.sentence"])

  # Extract the relation mention
  relation = relation_drug_gene.extract(sentence, mention1, mention2)
  
  json.dumps({
    "type":relation.type, 
    "mid1":relation.m1.id, 
    "mid2":relation.m2.id, 
    "is_correct":relation.is_correct,
    "features":relation.features
  })
