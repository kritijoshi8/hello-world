# -*- coding: utf-8 -*-
"""
Created on Fri Jun 01 12:26:16 2018

@author: Dell
"""

import numpy as np
import pandas as pd
df=pd.read_csv("stats_females.csv")

features=df.iloc[:,1:].values#set of independent datasets
labels=df.iloc[:,0:1].values#set of dependent datasets

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(features_train,labels_train)

pred=regressor.predict(features_test)
print regressor.score(features_train,labels_train)

import statsmodels.formula.api as sm
features=np.append(arr=np.ones((214,1)).astype(int),values=features,axis=1)
features_opt=features[:,[0,1,2,]]
regressor_OLS=sm.OLS(endog=labels,exog=features_opt).fit()
regressor_OLS.summary() 

print regressor_OLS.params[1]
print regressor_OLS.params[2]
 

