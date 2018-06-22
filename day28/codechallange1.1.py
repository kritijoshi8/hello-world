# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 11:44:41 2018

@author: Dell
"""

import pandas as pd

df1=pd.read_csv("Agra.csv")

df2=pd.read_csv("Lucknow.csv")

df3=pd.read_csv("Meerut.csv")

df4=pd.read_csv("Delhi.csv")



df1_n=df1.merge(df2,on='Unnamed: 0')
df=df1_n.merge(df3,on='Unnamed: 0')

features=df.iloc[:,1:]
labels=df4.iloc[:,1:]


#using linear regression model
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(features_train,labels_train)

labels_pred=regressor.predict(features_test)

print regressor.score(features_test,labels_test)



from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = regressor,  X= features_train, y= labels_train, cv = 10)
print ("mean accuracy is",accuracies.mean())
print (accuracies.std())

































