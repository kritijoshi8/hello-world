# -*- coding: utf-8 -*-
"""
Created on Thu May 17 10:35:50 2018

@author: Dell
"""
import string
user_input=raw_input("enter the text:").lower()
list1=list(user_input)


list2 = set(list1)

count = 0
for i in list2:
    if i in string.ascii_lowercase:
        count = count + 1

if count == 26:
    print "panagram"
else:
    print "No"
    
#version 2
    
user_input=raw_input("enter the text:").lower()

set1 = set(user_input)
count = 0

for i in set1:
    if i >= 'a' and i <= 'z':
        count = count + 1
if count == 26:
    print "YES"
else:
    print "NO"
    
    


    
