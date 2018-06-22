# -*- coding: utf-8 -*-
"""
Created on Wed May 23 10:12:47 2018

@author: Dell
"""

import re
lst=[]
while True:
    user_input=raw_input()
    if not user_input:
        break
    lst.append(user_input)
    
for i in lst:
    if re.match(r'[a-z0-9_-]+@[a-z0-9]+\.[a-z]{2,4}$',i):
        print i
    else:
        print "wrong"