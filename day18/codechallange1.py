# -*- coding: utf-8 -*-
"""
Created on Tue Jun 05 11:05:39 2018

@author: Dell
"""
import numpy as np
import pandas as pd

df=pd.read_csv("PastHires.csv")
 
features=df.iloc[:,0:6].values
labels=df.iloc[:,-1:].values 


from sklearn.preprocessing import LabelEncoder
labelencoder=LabelEncoder()
for i in [1,3,4,5]:
    features[:,i]=labelencoder.fit_transform(features[:,i])
labels[:,-1]=labelencoder.fit_transform(labels[:,-1])

view_f=pd.DataFrame(features)
view_l=pd.DataFrame(labels)

from sklearn.tree import DecisionTreeRegressor
regressor=DecisionTreeRegressor(random_state=0)
regressor.fit(features,labels)

print regressor.score(features,labels)

from sklearn.ensemble import RandomForestRegressor
regressor=RandomForestRegressor(n_estimators=10,random_state=0)
regressor.fit(features,labels)

param=np.array([10,'Y',4,'BS','Y','N']).reshape(1,-1)
for i in [1,3,4,5]:
    param[:,i]=labelencoder.transform(param[:,i])





