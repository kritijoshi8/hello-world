# -*- coding: utf-8 -*-
"""
Created on Fri May 25 13:12:26  

@author: Dell
"""

import pandas as pd
import numpy as np
df=pd.read_csv("Automobile.csv")
df["price"] = df["price"].fillna(df["price"].mean())
arr=np.array(df["price"])
print arr
print arr.min()
print arr.max()
print arr.mean()
print arr.std()