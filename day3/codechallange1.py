# -*- coding: utf-8 -*-
"""
Created on Tue May 15 19:03:52 2018

@author: Dell
"""

user_input=input("enter the values:")
x=map(int,user_input)
#here below we have defined the different functions.
def add(x,y):return x+y
def multiply(x,y):return x*y
def largest(x,y):return max(x,y)
def smallest(x,y):return min(x,y)
def sorting(x):
    x.sort()
    return x
def remove_duplicates(x):return set(user_input)
#here the print function has been defined.
def print1():
    print "sum is:",reduce(add,x)
    print "multiplication is:",reduce(multiply,x)
    print "largest value is:",reduce(largest,x)
    print "smallest value is:",reduce(smallest,x)
    print "sorted value is:",sorting(x)
    print "duplicate value is:",remove_duplicates(x)
    
print print1()