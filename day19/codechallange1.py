# -*- coding: utf-8 -*-
"""
Created on Wed Jun 06 10:26:13 2018

@author: Dell
"""
import numpy as np
import pandas as pd
df=pd.read_csv("affairs.csv")

features=df.iloc[:,0:-1].values
labels=df.iloc[:,-1].values

from sklearn.preprocessing import OneHotEncoder
onehotencoder=OneHotEncoder(categorical_features=[6])
features=onehotencoder.fit_transform(features).toarray()
features=features[:,1:]
onehotencoder=OneHotEncoder(categorical_features=[11])
features=onehotencoder.fit_transform(features).toarray()
features=features[:,1:]

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)

from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression(random_state=0)
classifier.fit(features_train,labels_train) 

labels_pred=classifier.predict(features_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(labels_test,labels_pred) 

correct=float(cm[0][0]+cm[1][1])
total=float(cm[0][0]+cm[0][1]+cm[1][0]+cm[1][1])

print "the score through confusion matrix is:",(correct/total) 

labels_pred= classifier.predict(features_test)
print df["affair"].value_counts(normalize=True)

Pred = classifier.predict(np.array([1,0,0,0,0,0,0,1,0,0,3,25,3,1,4,16]).reshape(1,-1))


# Building the optimal model
features=df.iloc[:,0:8].values
labels=df.iloc[:,8].values

import statsmodels.formula.api as sm
features = np.append(arr = np.ones((6366, 1)).astype(int), values = features, axis = 1)
features_opt = features[:, [0,1,2,3,4,5,6,7,8]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

features_opt = features[:, [0,1,2,3,5,6,7,8]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

features_opt = features[:, [0,1,2,3,5,6,7]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

print regressor_OLS.params[0]
print regressor_OLS.params[1]
print regressor_OLS.params[2]
print regressor_OLS.params[3]
print regressor_OLS.params[4]
print regressor_OLS.params[5]
print regressor_OLS.params[6]



























