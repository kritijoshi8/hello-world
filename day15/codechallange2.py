# -*- coding: utf-8 -*-
"""
Created on Thu May 31 11:48:45 2018

@author: Dell
"""

import pandas as pd
df=pd.read_csv("Bahubali2_vs_Dangal.csv")

features=df.iloc[:,0:1].values
labels1=df.iloc[:,1].values
labels2=df.iloc[:,2].values

from sklearn.model_selection import train_test_split
features_train,features_test,labels1_train,labels1_test=train_test_split(features,labels1,test_size=0.2,random_state=0)
features_train,features_test,labels2_train,labels2_test=train_test_split(features,labels2,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(features_train,labels1_train)
regressor.fit(features_train,labels2_train)

label_pred=regressor.predict(features_test)

print regressor.score(features_test,labels1_test)
print regressor.score(features_test,labels2_test)

print regressor.predict(10)