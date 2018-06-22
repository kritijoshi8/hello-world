# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:11:12 2018

@author: Dell
"""

from collections import OrderedDict
od=OrderedDict()
while True:
    user_input=raw_input()
    if not user_input:
        break
    
    list1=user_input.split(' ')
    
    value=list1[-1]
    key=' '.join(list1[0:-1])
    if key in od:
        od[key]=od[key]+int(value)
    else:
        od[key]=int(value)
        
for k,v in od.items():
    print k,v
    
    
    
    

                    
    
    