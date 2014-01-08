#! /usr/bin/env python

class Word(object):
    insent_id = None
    word = None
    pos = None
    ner = None
    lemma = None
    deppath = None
    deppar = None
    sentid = None
    box = None
    font = None
    centered = None
    followed = None
    left_margin = None
    altword = None

    def __init__(self, _insent_id, _word, _pos, _ner, _lemma, _deppath, _deppar, _sentid, _box):
        self.insent_id = int(_insent_id) - 1
        (self.word, self.pos, self.ner, self.lemma, self.deppath) = (_word, _pos, _ner, _lemma, _deppath)
        self.ner = self.ner
        self.deppar = int(_deppar) - 1
        self.sentid = int(_sentid.split('_')[-1]) - 1
        self.box = _box
        self.font = ""
        self.centered = False
        self.followed = False
        self.left_margin = 1000000
        self.altword = None

    def __repr__(self):
        return self.word

    def get_feature(self):
        if self.ner == 'O':
            if self.lemma == '"': 
                return "''"
            else: 
                return self.lemma
        else:
            return self.ner