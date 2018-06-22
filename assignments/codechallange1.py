# -*- coding: utf-8 -*-
"""
Created on Fri Jun 01 11:41:51 2018

@author: Dell
"""

import numpy as np
import pandas as pd 

data=pd.read_csv("iq_size.csv") 

features=data.iloc[:,1:].values#set of independent datasets
labels=data.iloc[:,0:1].values#set of dependent datasets 

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(features_train,labels_train)

pred=regressor.predict(features_test)
print regressor.predict(np.array([90,70,150]).reshape(1,-1))

Score=regressor.score(features_train,labels_train)

import statsmodels.formula.api as sm
features=np.append(arr=np.ones((38,1)).astype(int),values=features,axis=1)
features_opt=features[:,[0,1,2,3]]
regressor_OLS=sm.OLS(endog=labels,exog=features_opt).fit()
regressor_OLS.summary()
features_opt=features[:,[0,1,2,]]
regressor_OLS=sm.OLS(endog=labels,exog=features_opt).fit()
regressor_OLS.summary()
features_opt=features[:,[1,2,]]
regressor_OLS=sm.OLS(endog=labels,exog=features_opt).fit()
regressor_OLS.summary()
features_opt=features[:,[1]]
regressor_OLS=sm.OLS(endog=labels,exog=features_opt).fit()
regressor_OLS.summary()



                 
                 