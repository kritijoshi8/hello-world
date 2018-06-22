# -*- coding: utf-8 -*-
"""
Created on Tue May 15 20:11:11 2018

@author: Dell
"""
list1= list(input("enter the values:"))
smallest_brick=1
largest_brick=5
def wall_of_brick(list1):
    if(list1[0]*smallest_brick+list1[1]*largest_brick>=list1[2]):
        print "True"
    else:
        print "False"

print wall_of_brick(list1)

