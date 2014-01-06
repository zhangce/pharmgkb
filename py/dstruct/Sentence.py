#! /usr/bin/env python

class Sentence(object):

    sentid = None
    words = None

    def __init__(self):
        self.words = []
        self.sentid = None

    def __repr__(self):
        _words = []
        for w in self.words:
            _words.append(w.word)
        return " ".join(_words)
    
    def push_word(self, word):
        if self.sentid== None:
            self.sentid = word.sentid
            self.words.append(word)
            return True
        else:
            if self.sentid == word.sentid:
                self.words.append(word)
                return True
            else:
                return False

    def get_word_dep_path(self, idx1, idx2):
        
        path1 = []
        path2 = []

        c = idx1
        i = len(self.words) + 10
        while i > 0:
            i = i -1
            try:
                if c == -1: break
                path1.append(c)
                c = self.words[c].deppar
            except:
                break

        c = idx2
        i = len(self.words) + 10
        while i > 0:
            i = i -1
            try:
                if c == -1: break
                path2.append(c)
                c = self.words[c].deppar
            except:
                break

        parent = None
        for i in range(0, max(len(path1), len(path2))):
            tovisit = 0 - i - 1
            if i >= len(path1) or i >= len(path2):
                break
            if path1[tovisit] != path2[tovisit]:
                break
            parent = path1[tovisit]
        #print parent

        first_word_to_parent = []
        c = idx1   
        i = len(self.words) + 10
        while i > 0:
            i = i -1
            try:
                if c == -1: break
                if c == parent: break
                if c == idx1: 
                    first_word_to_parent.append(self.words[c].deppath)
                else:
                    first_word_to_parent.append(self.words[c].deppath + "|" + self.words[c].get_feature())
                    
                c = self.words[c].deppar
            except:
                break

        second_word_to_parent = []
        c = idx2
        i = len(self.words) + 10
        while i > 0:
            i = i -1
            try:
                if c == -1: break
                if c == parent: break
                if c == idx2:
                    second_word_to_parent.append(self.words[c].deppath)
                else:
                    second_word_to_parent.append(self.words[c].deppath + "|" + self.words[c].get_feature())
                    
                c = self.words[c].deppar   
            except:
                break

        #print first_word_to_parent
        #print second_word_to_parent

        return "-".join(first_word_to_parent) + "@" + "-".join(second_word_to_parent)

    def get_prev_wordobject(self, mention):
        begin = mention.prov_words[0].insent_id
        a = begin - 1
        if a < 0:
            return None
        else:
            return self.words[a]

    def get_dependency_rightside(self, mention):
        begin = mention.prov_words[0].insent_id
        end = mention.prov_words[-1].insent_id
        
        paths = []
        for i in range(begin, end+1):
            if self.words[i].deppar < begin or self.words[i].deppar > end:
                par = self.words[i].deppar
                path = "@ --" + self.words[i].deppath + "-->" + self.words[par].get_feature()

                for k in self.words[par].ner:
                    for mention2 in self.words[par].ner[k]:
                        if mention2 != None:
                            paths.append([mention, mention2, path])
                            #print mention, mention2, path
        return paths      


    def get_dependency_leftside(self, mention):
        begin = mention.prov_words[0].insent_id
        end = mention.prov_words[-1].insent_id
        
        paths = []
        for i in range(begin, end+1):
            if self.words[i].deppar < begin or self.words[i].deppar > end:

                has_word = False
                for w in range(0, len(self.words)):
                    if self.words[w].deppar == i:
                        final_path = self.words[w].get_feature() + " ~~" + self.words[w].deppath + "~~> " 
                        

                        for k in self.words[w].ner:
                            for mention2 in self.words[w].ner[k]:
                                if mention2 != None:
                                    #print mention, mention2, final_path
                                    paths.append([mention, mention2, final_path])

                        has_word = True

                if has_word == False:
                    for w in range(0, len(self.words)):
                        if self.words[w].deppar == self.words[i].deppar and w != i:
                            final_path = self.words[w].get_feature() + " ==" + self.words[w].deppath + "==> " 
                            
                            for k in self.words[w].ner:
                                for mention2 in self.words[w].ner[k]:
                                    if mention2 != None:
                                        #print mention, mention2, final_path
                                        paths.append([mention, mention2, final_path])

        return paths      

    def dep_parent(self, mention):
        begin = mention.prov_words[0].insent_id
        end = mention.prov_words[-1].insent_id
        
        paths = []
        for i in range(begin, end+1):
            if self.words[i].deppar < begin or self.words[i].deppar > end:
                par = self.words[i].deppar
                path = "@ --" + self.words[i].deppath + "-->" + self.words[par].get_feature()
                #paths.append(path)

                has_word = False
                for w in range(0, len(self.words)):
                    if self.words[w].deppar == i:
                        final_path = self.words[w].get_feature() + " ~~" + self.words[w].deppath + "~~> " + path
                        paths.append(final_path)
                        has_word = True

                if has_word == False:
                    for w in range(0, len(self.words)):
                        if self.words[w].deppar == self.words[i].deppar and w != i:
                            final_path = self.words[w].get_feature() + " ==" + self.words[w].deppath + "==> " + path
                            paths.append(final_path)
                            has_word = True

                if has_word == False:
                    final_path = "NULL ## " + path
                    paths.append(final_path)

        #path = ""
        #ll = 100000000
        #for p in paths:
        #    if len(p) < ll:
        #        path = p
        #        ll = len(p)
        return paths

    def dep_path(self, entity1, entity2):
    
        begin1 = entity1.prov_words[0].insent_id
        end1 = entity1.prov_words[-1].insent_id
        begin2 = entity2.prov_words[0].insent_id
        end2 = entity2.prov_words[-1].insent_id
    
        paths = []
        for idx1 in range(begin1, end1+1):
            for idx2 in range(begin2, end2+1):
                paths.append(self.get_word_dep_path(idx1, idx2))

        path = ""
        ll = 100000000
        for p in paths:
            if len(p) < ll:
                path = p
                ll = len(p)
        return path


    def wordseq_feature(self, entity1, entity2):
        
        begin1 = entity1.words[0].insent_id
        end1 = entity1.words[-1].insent_id
        begin2 = entity2.words[0].insent_id
        end2 = entity2.words[-1].insent_id

        start = end1 + 1
        finish = begin2 - 1
        prefix = ""

        if end2 <= begin1:
            start = end2 + 1
            finish = begin1 - 1
            prefix = "INV:"
        
        ss = []
        for w in range(start, finish + 1):
            ss.append(self.words[w].get_feature())

        return prefix + "_".join(ss)

    def wordseq_feature2(self, begin1, end1, begin2, end2):
        
        start = end1 + 1
        finish = begin2 - 1
        prefix = ""

        if end2 <= begin1:
            start = end2 + 1
            finish = begin1 - 1
            prefix = "INV:"
        
        ss = []
        for w in range(start, finish + 1):
            ss.append(self.words[w].get_feature())

        return prefix + "_".join(ss)







