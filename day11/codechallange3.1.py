# -*- coding: utf-8 -*-
"""
Created on Fri May 25 12:10:30 2018

@author: Dell
"""

import numpy as np
from collections import Counter
   
num=np.random.randint(5,15,40)
lst=list(num)
print num
counts=np.bincount(num)#counts the occurence of each element
print np.argmax(counts)#return the largest value from the list

num1= Counter(num)
print num1.most_common(1)

max(lst,key=lst.count)