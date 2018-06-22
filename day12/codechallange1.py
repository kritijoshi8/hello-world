# -*- coding: utf-8 -*-
"""
Created on Mon May 28 11:44:32 2018

@author: Dell
"""

import urllib2
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt




area="https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"
page=urllib2.urlopen(area)
soup=BeautifulSoup(page,"lxml")
tables=soup.find('table',class_="wikitable")

a=[]
b=[] 
c=0
for row in tables.find_all("tr"):
    if c == 7:
        break
    c += 1
    cells=row.find_all("td")
    if len(cells)==7:
        a.append(cells[1].text.strip())
        b.append(cells[4].text.strip())
    
    
import pandas as pd
df=pd.DataFrame()
df["country_name"]=a
df["%age_share"]=b
print df 

ax1 = plt.subplot()
explode = [0.2,0,0,0,0,0]
ax1.pie(b,explode, labels=a, autopct='%1.2f%%')
ax1.axis('equal') 
 
plt.show()




































