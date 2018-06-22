# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 11:21:42 2018

@author: Dell
"""

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("election_data.csv")

df=df.apply(lambda x:x.fillna(x.value_counts().index[0]))




plt.rcdefaults()









































































