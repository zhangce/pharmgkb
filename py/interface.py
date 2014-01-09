
import os
import re
import sys
import psycopg2

from dstruct.Box import *
from helper.easierlife import *

INPUT_FOLDER = BASE_FOLDER + "/input/"

docid = sys.argv[1]
relations = sys.argv[2].split(',')

conn_string = "host='localhost' dbname='deepdive_titles' user='czhang' password='bB19871121'"
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()

class Boxes:
	boxes = []

highlights = {}

ratio = 1.0*480/2163

for relation in relations:

	SQL = """
    	SELECT object FROM %s_is_correct_inference where probability > 0.0 
    	AND docid = '%s';
	""" % (relation, docid)

	cursor.execute(SQL)

	for record in cursor.fetchall():
		mention = deserialize(record[0])

		b = Boxes()
		for w in mention.prov_words:
			bb = Box(w.box)
			bb.left = ratio * bb.left
			bb.right = ratio * bb.right
			bb.top = ratio * bb.top
			bb.bottom = ratio * bb.bottom

			b.boxes.append(bb)

		highlights[b] = mention


#page2box = {}
#for boxes in highlights:
#	if b.page not in page2box:
#		page2box[b.page] = []
#	page2box[b.page].append(b)


def getoverlay(box, color):
        return '<div style="position:relative;left:%dpx;top:%dpx;width:%dpx;height:%dpx;background-color:%s;opacity:0.5;"></div>' % (box.left, box.top, box.right, box.bottom-box.top, color)

pages = []
for f in os.listdir(INPUT_FOLDER + "/" + docid):
	if not f.endswith('.png'): continue
	m = re.search('page-(.*?).png', f)
	if m:
		pages.append(int(m.group(1)))

pages = sorted(pages)

print '<table>'
for page in pages:
	#print '<tr><td>'
	print '<div style="position: relative;>'
	print '<img src="%s" width="640px"/>' % (INPUT_FOLDER + "/" + docid + "/page-%d.png" % (page))
	for boxes in highlights:
		for box in boxes.boxes:
			if box.page == page:
				print getoverlay(box, "red")
	print '</div>'
	#print '</td></tr>'
print '</table>'


