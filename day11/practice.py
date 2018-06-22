# -*- coding: utf-8 -*-
"""
Created on Fri May 25 10:26:10 2018

@author: Dell
"""

import numpy as np
x=np.array([[1,2,3],[4,5,6]],np.int32)
print type(x)
print x.shape
print x.dtype #by default storage is of 8 byte=64 bits


import numpy as np
x=np.float32(1.0)
print x

y=np.int_([1,2,3])
print y 

z=np.arange(3,dtype=np.uint8)
print z
print z.dtype


x=np.zeros((2,3))
print x 

x=np.ones((2,3),dtype=np.int8)
print x

print np.arange(10)

x=np.linspace(1,4,6)
print x 

print np.random.random((2,3))

a=np.arange(9)
print a

b=a.reshape(3,3)
print b 


a=np.arange(5)
b=np.arange(5)

print a+b
print a-b
print a**2
print a>3#return answer in boolean
print 10*np.sin(a)
print a*b

incomes=np.random.normal(27000,560000,678900)
np.mean(incomes) 

import matplotlib.pyplot as plt
plt.hist(incomes,20)
plt.show()















































