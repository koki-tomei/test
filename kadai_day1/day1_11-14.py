# -*- coding: utf-8 -*-
"""
open("dataset/data.txt","r",encoding="UTF-8")
sen=f.read()
f.close()
print(sen)"""

import numpy as np
#11
print("===11===")

with open("dataset/data.txt","r",encoding="UTF-8") as f:
    for line in f:
        print(line,end="")
print()

#12
print("===12===")
def get_dt(path):
    docs=[]
    with open(path,"r",encoding="UTF-8") as f:
        for line in f:
            line=line.replace("\n","")
            words=line.split("と")
            docs.append(words)
    
    
    terms=[]
    for li in docs:
        terms+=li
    terms=list(set(terms))
    return docs,terms

docs,terms =get_dt("dataset/data.txt")

print("docs:"+str(docs))
print("terms:"+str(terms))

#13
print("===13===")
def tf(term,doc):
    tfv=doc.count(term)/len(doc)
    return tfv
print(tf('リンゴ', ['リンゴ', 'リンゴ']))
print(tf('レモン', ['リンゴ', 'レモン']))

#14
print("===14===")
def idf(term,docs):
    tr_doc=[x for x in docs if tf(term,x)>0]
    idfv =np.log10( len(docs)/len(tr_doc) ) +1
    return idfv

docs=[["リンゴ", "リンゴ"], ["リンゴ", "レモン"], ["レモン", "ミカン"]]
print(idf("リンゴ",docs))
print(idf("レモン",docs))
print(idf("ミカン",docs))


