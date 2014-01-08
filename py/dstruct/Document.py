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

    sents = None

    def __init__(self, _docid):

        self.docid = _docid
        self.sents = []
        self.sents.append(Sentence())
    
    def parse_doc(self, filepath):
        
        try:
            for l in open(filepath + "/input.text"):
                ss = l.rstrip().split('\t')
                if len(ss) < 3: continue
                (insent_id, word, pos, ner, lemma, deppath, deppar, sentid, box) = ss
                self.push_word(Word(insent_id, word, pos, ner, lemma, deppath, deppar, sentid, box))
        except:
            return

    def push_word(self, word):

        if self.sents[-1].push_word(word) == False:
            self.sents.append(Sentence())
            self.sents[-1].push_word(word)


