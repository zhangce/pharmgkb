#! /usr/bin/env python

import codecs
from multiprocessing import *

from helper.easierlife import *

from dstruct.Document import *


for row in get_inputs():
	docid = row["docids.docid"]
	folder = row["docids.folder"]
	doc = Document(docid)
	doc.parse_doc(folder)
	print json.dumps({"docid":docid, "document":serialize(doc)})








