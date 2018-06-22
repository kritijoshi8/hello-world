# -*- coding: utf-8 -*-
"""
Created on Tue May 22 11:08:53 2018

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
    if re.match(r'^[+-]?\d*\.\d+$',i):
        print "true"
    else:
        print "false"
    
