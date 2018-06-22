# -*- coding: utf-8 -*-
"""
Created on Fri May 11 10:25:16 2018

@author: Dell
"""

str1 ="forsk jaipur"
str2 ="""doc string"""
print str1.upper()
print str1[::-1]
print str1.find('a')
str2=str1.replace('a','A')
print str2
str="welcome to summer bootcamp"
str.split()
type(str.split('m'))
'boot' in str
" ".join(['hello','world'])
str.join(['hello','world'])
"india".join(['hello','world'])
a="python"
b="hello"
print "%s %s" % (a,b)
print 'chapter %d:%s' % (2,'english')

str1="   welcome           jaipur".strip()
a=str1.find(" ")
print str1[a+1:].strip(),str1[:a].strip() 
print str1[0:a].strip(),str1[a:].lstrip() 