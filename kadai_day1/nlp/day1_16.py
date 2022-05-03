# -*- coding: utf-8 -*-
import numpy as np

def cosine_sim(x1,x2):
    csim =np.dot(x1,x2)/( np.linalg.norm(x1)*np.linalg.norm(x2) )
    return csim

if __name__=="__main__":
    x1 = np.array([1, 0, 0, 1])
    x2 = np.array([0, 1, 0, 1])
    print(cosine_sim(x1,x2))