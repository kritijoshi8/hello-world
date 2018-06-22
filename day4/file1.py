# -*- coding: utf-8 -*-
"""
Created on Wed May 16 10:32:30 2018

@author: Dell
"""

fp =open("test2.txt")
type(fp)

fp.read()
print fp.read()

fp.close()
fp=open("test.txt")
fp.readline() 

fp.seek(0,0)  #we can move the file pointer to any location 
              #0 specifies beginning,1 specifies current position ,2 secifies end of the file
fp.readline()
fp.readlines() #specifies  the values in the form of text

for line in fp:
    print line

fp=open("test.txt","w")