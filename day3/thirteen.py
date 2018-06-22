# -*- coding: utf-8 -*-
"""
Created on Tue May 15 13:41:22 2018

@author: Dell
"""

lst = list(input("Enter num: "))

flag = 0
total = 0

for i in lst:
    if i == 13:
        flag = 1
    if flag == 0:
        total += i
    elif flag == 1 and i != 13:
        flag = 0

print total