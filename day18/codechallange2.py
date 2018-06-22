# -*- coding: utf-8 -*-
"""
Created on Tue Jun 05 12:32:33 2018

@author: Dell
"""
import pandas as pd
import numpy as np

df=pd.read_fwf("note.txt",header=None)
df.columns=["mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name" ]

df['horsepower']=df['horsepower'].replace('?',df['horsepower'].value_counts().index[0])
f_mpg=df.groupby(["mpg"])
print f_mpg["car name"].value_counts().index[-1]
df['horsepower']=pd.to_numeric(df['horsepower'])


features=df.iloc[:,1:-1].values
labels=df.iloc[:,0].values
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)
 

from sklearn.tree import DecisionTreeRegressor
regressor1=DecisionTreeRegressor(random_state=0)
regressor1.fit(features_train,labels_train)

print regressor1.score(features_test,labels_test)
print regressor1.predict(np.array([6,215,"100",2630,22.2,80,3]).reshape(1,-1))

from sklearn.ensemble import RandomForestRegressor
regressor2=RandomForestRegressor(n_estimators=10,random_state=0)
regressor2.fit(features_train,labels_train)
print regressor2.score(features_test,labels_test) 
print regressor2.predict(np.array([6,215,"100",2630,22.2,80,3]).reshape(1,-1)) 


