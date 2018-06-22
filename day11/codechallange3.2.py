# -*- coding: utf-8 -*-
"""
Created on Fri May 25 12:45:24 2018

@author: Dell
"""

import numpy as np
user_input=raw_input().split(' ')
list1=[]
for i in user_input:
    list1.append(int(i))
print list1

arr=np.array(list1)
final_arr=arr.reshape(3,3)
print final_arr