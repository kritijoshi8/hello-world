# -*- coding: utf-8 -*-
"""
Created on Thu May 24 12:41:57 2018

@author: Dell
"""

import pandas as pd

df=pd.read_csv("training_titanic.csv") 

df['Age'] = df['Age'].fillna(df['Age'].mean())

df['Child'] =0
df['Child'][df['Age']<18]=1 

df['Child'].value_counts()
df['Child'].value_counts(normalize=True)





