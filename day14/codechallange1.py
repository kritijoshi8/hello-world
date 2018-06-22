# -*- coding: utf-8 -*-
"""
Created on Wed May 30 10:28:45 2018

@author: Dell
"""

import pandas as pd
df= pd.read_csv (
               'https://raw.githubusercontent.com/rasbt/pattern_classification/master/data/wine_data.csv',
                header=None,
                usecols=[0,1,2]
                )
df.columns=['Class label','Alcohol','Malic Acid']

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
dataf1=sc.fit_transform(df)


from sklearn.preprocessing import MinMaxScaler
mm=MinMaxScaler()
dataf2=mm.fit_transform(df)

