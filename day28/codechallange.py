# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 11:10:18 2018

@author: Dell
"""
import pandas as pd
import urllib2, re
from bs4 import BeautifulSoup
df=pd.DataFrame()
i=raw_input("city name")
weather="https://www.timeanddate.com/weather/india/"+i+"/hourly"
page=urllib2.urlopen(weather)
soup=BeautifulSoup(page,"lxml")
tables=soup.find_all('table',class_='zebra')
a=[]
b=[]
c=[]     
for row in tables:
    row=row.find("tbody")
    rows=row.find_all("tr")
    for cells in rows:
        cells=cells.find_all("td")
        a.append(re.sub("[^0-9]", " ", cells[1].text.encode('utf-8').strip()))
        b.append(re.sub("[^0-9]", " ", cells[4].text.encode('utf-8').strip()))
        c.append(re.sub("[^0-9]", " ", cells[6].text.encode('utf-8').strip()))
        
df["temprature of"+i]=a
df["wind of"+i]=b
df["humidity of"+i]=c
df.to_csv(i+".csv")

                

            



