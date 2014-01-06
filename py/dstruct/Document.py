#! /usr/bin/env python

import math
import copy
import re

from helper.easierlife import *

from dstruct.Sentence import *
from dstruct.Word import *
from dstruct.Box import *


class Document(object):

    docid = None

    title = None

    sents = None
    
    candidate_drug_mentions = None

    candidate_gene_mentions = None

    candidate_motabolite_mentions = None

    candidate_pathway_mentions = None

    candidate_relation_mentions = None

    dependencies = None

    def __init__(self, _docid):

        self.docid = _docid
        self.title = ""
        self.sents = []
        self.sents.append(Sentence())
    
        self.candidate_pathway_mentions = {}
        self.candidate_gene_mentions = {}
        self.candidate_motabolite_mentions = {}
        self.candidate_drug_mentions = {}
        self.candidate_relation_mentions = {}
        self.dependencies = []
    
    def parse_doc(self, filepath):

        lastbox = None
        newsentidct = 1
        lastsentid = None
        reallastbox = None
        insentid_ct = 0
        
        try:
            for l in open(filepath + "/title.text"):
                self.title = l.rstrip()
        except:
            self.title = ""

        try:
            for l in open(filepath + "/input.text"):
                ss = l.rstrip().split('\t')
                if len(ss) < 3: continue
                (insent_id, word, pos, ner, lemma, deppath, deppar, sentid, box) = ss
                
                box = Box(box)
            
                if lastsentid == None:
                    insentid_ct = 0
                    lastbox = box
                    reallastbox = box
                    lastsentid = sentid
                    newsentid = "SENT_%d" % newsentidct
                else:
                    if lastsentid != sentid:
                        insentid_ct = 0
                        lastbox = box
                        reallastbox = box
                        lastsentid = sentid
                        newsentidct = newsentidct + 1
                        newsentid = "SENT_%d" % newsentidct
                    else:
                        reallastbox = box
                        lastsentid = sentid
                        newsentid = "SENT_%d" % newsentidct

                insentid_ct = insentid_ct + 1
        
                self.push_word(Word("%d"%insentid_ct, word, pos, ner, lemma, deppath, deppar, newsentid, box))
        except:
            donothing = False

    def push_word(self, word):

        if self.sents[-1].push_word(word) == False:
            self.sents.append(Sentence())
            self.sents[-1].push_word(word)
        #if word.sentid not in self.entities:
        #    self.entities[word.sentid] = []
    
    def update_word_ner(self, mention):
        for word in mention.prov_words:
            if mention.type not in word.ner:
                word.ner[mention.type] = []
            word.ner[mention.type].append(mention)


    def add_dependencies(self, dep):
        self.dependencies.append(dep)

    def add_candidate_drug_mentions(self, sentid, mention):
        if sentid not in self.candidate_drug_mentions:
            self.candidate_drug_mentions[sentid] = []
        self.candidate_drug_mentions[sentid].append(mention)
        self.update_word_ner(mention)

    def add_candidate_gene_mentions(self, sentid, mention):
        if sentid not in self.candidate_gene_mentions:
            self.candidate_gene_mentions[sentid] = []
        self.candidate_gene_mentions[sentid].append(mention)
        self.update_word_ner(mention)

    def add_candidate_motabolite_mentions(self, sentid, mention):
        if sentid not in self.candidate_motabolite_mentions:
            self.candidate_motabolite_mentions[sentid] = []
        self.candidate_motabolite_mentions[sentid].append(mention)
        self.update_word_ner(mention)

    def add_candidate_pathway_mentions(self, sentid, mention):
        if sentid not in self.candidate_pathway_mentions:
            self.candidate_pathway_mentions[sentid] = []
        self.candidate_pathway_mentions[sentid].append(mention)
        self.update_word_ner(mention)

    def add_candidate_relation_mentions(self, sentid, mention):
        if sentid not in self.candidate_relation_mentions:
            self.candidate_relation_mentions[sentid] = []
        self.candidate_relation_mentions[sentid].append(mention)

    def dump(self, fo):

        mid2id = {}
        for dicts in [self.candidate_gene_mentions, self.candidate_drug_mentions, self.candidate_motabolite_mentions]:
            for sentid in dicts:
                for m in dicts[sentid]:
                    if m not in mid2id: mid2id[m] = len(mid2id) + 1
                    m.id = "DOC_" + self.docid + "_MID_%d" % mid2id[m]

        rs = {}
        rs["docid"] = self.docid
        rs["candidate_gene_mentions"] = serialize(self.candidate_gene_mentions)
        rs["candidate_drug_mentions"] = serialize(self.candidate_drug_mentions)
        rs["candidate_motabolite_mentions"] = serialize(self.candidate_motabolite_mentions)
        rs["candidate_relation_mentions"] = serialize(self.candidate_relation_mentions)
        rs["dependencies"] = serialize(self.dependencies)
        fo.write(json.dumps(rs))






