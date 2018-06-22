# -*- coding: utf-8 -*-
"""
Created on Mon May 14 11:37:20 2018

@author: Dell
"""

list1=raw_input("enter the list")
print list1

user_input=raw_input("enter the values")
list2=list(user_input)
list3=user_input.split(',')
print list3



tuple1=raw_input("enter the values")
tuple2=tuple(tuple1)
tuple3=tuple1.split(',')
print tuple3

     
numbers=[386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527]

for item in numbers:
    if item==237:
        break
    else:
        if item%2==0:
            print item 
          
user_input=raw_input("enter the statement")
user_input1=list(user_input)
print user_input1
dict1={}
for item in user_input1:
    print (item,user_input.count(item))
    dict1[item]=user_input.count(item)
print dict1

user_input=raw_input("enter the statement")
count1=0
count2=0
for value in user_input:
    if(value.isdigit()):
        count1=count1+1
    else:
        if(value.isalpha()):
            count2=count2+1
            
print count1
print count2
    
user_input=input("enter the values")
list1=list(user_input)
list1.sort()
list2=list1[1:-1]
sum1=sum(list2)
size = len(list2)
    
print sum1/size


user_input=input("enter the list of elements")
list1=list(user_input)
index=0
sum1=0
while index<len(list1):
    if list1[index]==13:
        sum1=sum1+int(list1[index+2])
        index=index+2
    else:
        sum1=sum1+int(list1[index])
    index=index+1;
print sum1
        

    
        
        



























    
    
    

    



    













            

    
    

