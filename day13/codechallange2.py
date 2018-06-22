# -*- coding: utf-8 -*-
"""
Created on Tue May, 29 14:01:37 2018

@author: Dell
"""

import pandas as pd
data=pd.read_csv("Loan.csv")

features=data.iloc[:,1:-1].values
labels=data.iloc[:,-1].values

from sklearn.preprocessing import LabelEncoder
labelencoder=LabelEncoder() 

for i in [0,1,2,3,4,-1]:
    features[:,i]=labelencoder.fit_transform(features[:,i])
    
labels=labelencoder.fit_transform(labels)

from sklearn.preprocessing import OneHotEncoder
onehotencoder=OneHotEncoder(categorical_features=[-1])
features=onehotencoder.fit_transform(features).toarray()

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_split=train_test_split(features,labels, test_size=0.2 ,random_state = 0)

