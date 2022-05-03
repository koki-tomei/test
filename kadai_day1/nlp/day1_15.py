# -*- coding: utf-8 -*-
import numpy as np
def tf(term,doc):
    tfv=doc.count(term)/len(doc)
    return tfv
def idf(term,docs):
    tr_doc=[x for x in docs if tf(term,x)>0]
    idfv =np.log10( len(docs)/len(tr_doc) ) +1
    return idfv



def tfidf(term,doc,docs):
    tfidfv=tf(term,doc) * idf(term,docs)
    return tfidfv
def ti_matrix(terms,docs):
    ret =[]
    for doc in docs:
        ret.append( [tfidf(term,doc,docs) for term in terms] )
    return ret

if __name__=="__main__":
    docs = [["リンゴ", "リンゴ"], ["リンゴ", "レモン"], ["レモン", "ミカン"]]
    terms = ["リンゴ", "レモン", "ミカン"]
    print(ti_matrix(terms,docs))