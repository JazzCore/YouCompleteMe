#!/usr/bin/env python
# encoding: utf-8

class Completion(object):
    def __init__(self, word, menu):
        self.word = word
        self.menu = menu

def make_completion_list(lst, kind):
    ret = []

    with open('dicts/'+lst) as f:
        for line in f:
            #TODO respect kind
            tokens = line.split(';')
            ret.append(Completion(tokens[0].strip(),tokens[1].strip()))

    return ret

make_completion_list('functions.dict', 1)
