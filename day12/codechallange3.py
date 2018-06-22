# -*- coding: utf-8 -*-
"""
Created on Mon May 28 13:59:31 2018

@author: Dell
"""

import pandas as pd
dataset=pd.read_csv("Cars.csv")
col=list(dataset.columns)

features=dataset.iloc[:,1:].values#independent_datasets
labels=dataset.iloc[:,0].values#dependent datasets

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features,labels, test_size=0.2 ,random_state = 0)
print features_train
print features_test 
print labels_train 
print labels_test

df1=pd.DataFrame(features_train,columns=col[1:])
df1.to_csv("features_train.csv",index=False)

df2=pd.DataFrame(features_test,columns=col[1:])
df2.to_csv("features_test.csv",index=False)

df3=pd.DataFrame(labels_train)
df3.to_csv("labels_train.csv",index=False)

df4=pd.DataFrame(labels_test)
df4.to_csv("labels_test.csv",index=False)   