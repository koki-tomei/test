# -*- coding: utf-8 -*-
import numpy as np
from nlp import day1_15
from nlp import day1_16

def cos_docs(terms,docs):
    tim=day1_15.ti_matrix(terms, docs)
    cosm=[]
    for tiv1 in tim:
        cosm.append([day1_16.cosine_sim(tiv1,tiv2) for tiv2 in tim])
    return cosm

docs=[['リンゴ', 'リンゴ', 'リンゴ'], ['リンゴ', 'レモン', 'レモン', 'ミカン'], ['リンゴ', 'イチゴ', 'ミカン'], ['レモン', 'イチゴ', 'ミカン'], ['ミカン', 'ミカン', 'ブドウ', 'ブドウ']]
terms=['レモン', 'ブドウ', 'ミカン', 'イチゴ', 'リンゴ']
print(cos_docs(terms, docs))