# -*- coding: utf-8 -*-
"""
Created on Mon May 21 10:14:47 2018

@author: Dell
"""

#collections.Counter()
#a counter is a container that stores elements as dictionary and their counts are stored as dictionary value.

from collections import Counter
mylist=[1,1,2,3,4,5,3,2,3,4,2,1,2]
cnt=Counter(mylist)
Counter(mylist)

#default dictionary #for the dictionary to be in specific order
s="acfdfndcndknfemncfkenfek"
from collections import defaultdict
dd=defaultdict(int)
for key in s:
    dd[key]+=1 #if a key does not exists it creates one.
    
print dd

#orderd dictionary: order is intact
ordinary_dictionary={}
ordinary_dictionary["a"]=1

from collections import Ordereddict
ordinary_dictionary= Ordereddict()


#named tuple:can take tuple inputs and its name also its parameters
from collections import namedtuple
Point = namedtuple('point','x,y')


#zip:will zip the number of items given to it
print zip([1,2,3,4,5,6],'hacker') #two lists can also be zipped

a=[1,2,3]
b=[4,5,6]
c=[7,8,9]

print zip(a,b,c)

all([])#gives true if all conditions are true and just opposite with "ANY"

def sumprod(a,b):
    return a+b,a*b

s,p =sumprod(2,3)#unpacking 

def sumitall(*values):#multiple arguments can be passed
    total=0
    for i in values:
        total += i
    return total

sumitall(2,3,4,5)

sumitall(2,3)





























