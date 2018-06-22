# -*- coding: utf-8 -*-
"""
Created on Thu May 24 11:57:44 2018

@author: Dell
"""

import pandas as pd

df=pd.read_csv("training_titanic.csv")

df["Survived"].value_counts()

df["Survived"].value_counts(normalize= True)[1]

df_sex=df.groupby(["Sex"])

df_sex["Survived"].value_counts()

df_sex["Survived"].value_counts(normalize= True)


df['Survived'].value_counts()[df['Sex']=='male']



