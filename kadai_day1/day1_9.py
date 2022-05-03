# -*- coding: utf-8 -*-
import random
import sys

args=sys.argv[1:]

ret=""

def rnd_str(s):
  r=random.sample(s,len(s))
  return "".join(r)

for w in args:
  if(len(w)<=3):
    ret+=w
  else:
    reti=w[0]
    reti+=rnd_str(w[1:-1])
    reti+=w[-1]
    ret+=reti
  ret+=" "

print(ret)
