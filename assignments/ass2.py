# -*- coding: utf-8 -*-
"""
Created on Wed May 30 23:59:42 2018

@author: Dell
"""

import urllib2
from bs4 import BeautifulSoup

astro="https://www.astrology.com/horoscope/daily/cancer.html"

signs=raw_input("enter the signs for which you want to view the horscope")

page=urllib2.urlopen(astro)

soup=BeautifulSoup(page,"lxml") 

data=soup.find('div',class_='daily-horoscope')
data=soup.find('p')

print data.text