# -*- coding: utf-8 -*-
"""
Created on Mon May 21 13:37:13 2018

@author: Dell
"""
while True:
    user_input=raw_input()
    if not user_input:
        break
    usr_lst = user_input.split()
    
    
list1 = []
list2 = []

for item in usr_lst:
    if int(item) > 0:
        list1.append(True)
    else:
        list1.append(False)
        
    if item == item[::-1]:
        list2.append(True)
    else:
        list2.append(False)
        
print all([all(list1), any(list2)])   



    


