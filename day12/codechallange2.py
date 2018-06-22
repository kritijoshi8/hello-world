# -*- coding: utf-8 -*-
"""
Created on Mon May 28 12:57:10 2018

@author: Dell
"""

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Automobile.csv") 

df1=pd.DataFrame()
df1=df["make"].value_counts() 

make_value=df1.head(10)
make_name=list(make_value.index)
comp=max(make_value)
explode=[]
for i in make_value:
    if i==comp:
        explode.append(0.2)
    else:
        explode.append(0)

ax1 = plt.subplot()
ax1.pie(make_value,explode,make_name, autopct='%1.2f%%')
ax1.axis('equal') 
 
plt.show()

#-----------------------------------------------------------------------------

df1=df["make"].value_counts() 
df2=pd.DataFrame({'make':df1.index,'values':df1.values})
ax1=plt.subplot()
sizes=df2.iloc[0:10,1].values
ax1.axis('equal')
ax1.pie(sizes,explode,labels=df2.iloc[0:10,0].values,autopct='%1.2f%%')
plt.show()



















