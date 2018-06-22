# -*- coding: utf-8 -*-
"""
Created on Tue May 22 13:31:30 2018

@author: Dell
"""

import urllib2
from bs4 import BeautifulSoup

cric="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
page=urllib2.urlopen(cric)
soup=BeautifulSoup(page) 
all_tables=soup.find_all('tbody')


a=[]
b=[]
c=[]
d=[]
e=[]
for row in all_tables[0].findAll("tr"):
    cells=row.findAll("td")
    a.append(cells[0].text.strip())
    b.append(cells[1].text.strip())
    c.append(cells[2].text.strip())
    d.append(cells[3].text.strip())
    e.append(cells[4].text.strip())
    
import pandas as pd
df=pd.DataFrame()
df["position"]=a
df["team"]=b
df["matches"]=c
df["points"]=d
df["ratings"]=e 
print df





















