# -*- coding: utf-8 -*-
"""
Created on Wed May 16 12:45:30 2018

@author: Dell
"""

user_input=raw_input("enter the string")

def translate(user_input):
    str2=""
    
    for i in user_input:
        if i not in ["a","e","i","o","u"]:
            str2=str2+ i+"o"+i
            
        else:
            str2=str2+i
    print str2
            
translate(user_input)
    
        