# -*- coding: utf-8 -*-
"""
Created on Tue May 22 10:33:18 2018

@author: Dell
"""

import re #imports regural expression
#match()checks for only at the beginning
#search() check for first occurence
#find all()searches all and returns a list
#find at same as find all but returns an object
#methods like start() and end() can be used to know start and end positions.

result=re.match(r'For', 'Forsk Summer Bootcamp')
print result.start()
print result.end()

pattern=re.compile('For')
result=pattern.findall('Forsk Summer Bootcamp')
print result 

result=re.findall(r'@\w+.\w+','xyz@gmail.com')
print result