# -*- coding: utf-8 -*-
"""
Created on Mon May 21 11:27:17 2018

@author: Dell
"""
list1=[]
while True: 
    user_input=raw_input()
    if not user_input:
        break
    tup1=user_input.split(',')
    list1.append((tup1[0], int(tup1[1]), int(tup1[2])))
    
list1.sort()
print list1 










 