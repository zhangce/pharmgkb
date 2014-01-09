#! /usr/bin/env python

from helper.easierlife import *

from dstruct.Document import *
from dstruct.Word import *

for row in get_inputs():
    docid = row["docids.docid"]
    folder = row["docids.folder"]
    log(docid)
    doc = Document(docid)

    try:
      for l in open(folder + "/input.text"):
        ss = l.rstrip().split('\t')
        if len(ss) < 3: continue
        (insent_id, word, pos, ner, lemma, deppath, deppar, sentid, box) = ss
        doc.push_word(Word(insent_id, word, pos, ner, lemma, deppath, deppar, sentid, box))
    except:
      continue

    print json.dumps({
      "docid":docid, 
      "document":serialize(doc)
      })








