# -*- coding: utf-8 -*-

import sys

args=sys.argv[1:]

def ngram(seq,n):
  ret_len=len(seq)-n+1
  ret_li=[]
  for i in range(ret_len):
    ret_li.append(seq[i:i+n])
  return ret_li

print(ngram(args,2))
print(ngram("".join(args),2))