# -*- coding: utf-8 -*-
"""
Created on Tue May 15 10:30:54 2018

@author: Dell
"""

a=[1,2]
b=[1,2]
a is b 
a==b 
c=a
a is c
def add_two_numbers(a,b):
    return a+b
add_two_numbers(2,4)
add_two_numbers(b=2,a=7)

def add(a,b):
    print a+b
 
    
add(2,3)
print add(2,3) 

def explain_python():
    """print a message explaining what pythin is"""
    print('pyhton is not a snake')
    print('python is a programming language')
explain_python.func_doc 
range(0,24)


def f(x):return x%3==0 or x%5==0 
filter(f,range(2,25)) #filtering is possible,returns result for every true value


def cube(x):return x*x*x 
map(cube,range(1,11)) #filtering is not done,returns result for every value
map(lambda x:x*x*x,range(1,11))#lamba is anonymous function.

def add(x,y):return x+y
reduce(add,range(1,11))#adding up of all the values.

a=[1,2,3]
[x**2 for x in a]
[x + 1 for x in [x ** 2 for x in a]]

list1=['it','is','raining','cats','and','dogs']
map(lambda word:len(word),list1)



























    