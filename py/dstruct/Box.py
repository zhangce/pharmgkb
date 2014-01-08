#! /usr/bin/env python

import re

class Box(object):
    
    left = None
    right = None
    top = None
    bottom = None
    page = None
    strform = ""

    def __init__(self, str):
        m = re.search('p([0-9]*)l([0-9]*)t([0-9]*)r([0-9]*)b([0-9]*)', str)
        if m: 
            (self.page, self.left, self.top, self.right, self.bottom) = (int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5)))
        self.strform = str

    def __repr__(self):
        return self.strform

    def overlap(self, b2):
        if self.page == b2.page:
            hoverlap = (self.right-self.left) + (b2.right-b2.left) - (max(self.right, b2.right) - min(self.left, b2.left))
            voverlap = (self.bottom-self.top) + (b2.bottom-b2.top) - (max(self.bottom, b2.bottom) - min(self.top, b2.top))
            if hoverlap >=0 and voverlap >=0:
                return True
        return False
            
