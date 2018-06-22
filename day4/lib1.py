# -*- coding: utf-8 -*-
"""
Created on Wed May 16 10:59:24 2018

@author: Dell
"""

import zlib
s="python is used extensively in industriesdasdgisahd siduhsauhdsahdhsad iauhdiusahasdqejiwfsa sadsadkmsadksamkdmsad nkdnkjsandjsandkjsandkjasnd"
len(s)
t=zlib.compress(s)
len(t)

zlib.decompress(t) 


import urllib2
f = urllib2.urlopen("http://www.forsk.in/")
f.read(1000)

import os
os.getcwd()
