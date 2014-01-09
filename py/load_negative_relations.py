#! /usr/bin/env pypy

from helper.easierlife import *
from extractor.RelationExtractor_DrugGene import *

# Initialize the extractor
relation_drug_gene = RelationExtractor_DrugGene()
relation_drug_gene.loadDict()

for row in get_inputs():
  mention1 = deserialize(row["gene_mentions.m1"])
  mention2 = deserialize(row["gene_mentions.m2"])
  sentence = deserialize(row["sentences.sentence"])

  # Use this relation mention as negative evidence
  relation = RelationMention("DrugGene", mention1, mention2)
  relation.add_features([sentence.dep_path(mention1, mention2),])
  relation.is_correct = False
  
  print json.dumps({
    "type":relation.type, 
    "mid1":relation.m1.id, 
    "mid2":relation.m2.id, 
    "is_correct":relation.is_correct,
    "features":relation.features
  })