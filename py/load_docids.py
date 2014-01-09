#! /usr/bin/env pypy

from helper.easierlife import *

INPUT_FOLDER = BASE_FOLDER + "/input"

for docid in os.listdir(INPUT_FOLDER):
	if docid.startswith('.'): continue
	folder = INPUT_FOLDER + "/" + docid
	print json.dumps({"docid": docid, "folder": folder})

