# -*- coding: utf-8 :-*-
"""
Created on Fri May 11 10:55:41 2018

@author: Dell
"""

str1="this is a multi line string. This code challange is to test your understanding about strings.You need to print some part of the string.From here print some part of the text without counting the indexes"
str2 = str1.find('From')
print str2
print(str1[str2:]) #code 1 follows


str=raw_input("str")
print str.replace(" ","*")
"*".join(str)    #code 2 and 3 follows


str2=raw_input("str")
str = str2.find(" ")
print str2[str:],str2[0:str] #code 4 follows

str1="Forsk Technologies"
print str1[-7:]
words = str1.split(' ')
','.join(words)
str1.split(' ',3)

_2 ="Harry Potter"

os="Mac OS"
ver="6s"
mob="iphone"
print 'I have an {0} uses {2} and model {1}'.format(mob,ver,os)

str1= "A string is a sequence of zero or more characters"
str1.split(' ',5)










