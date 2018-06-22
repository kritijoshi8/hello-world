# -*- coding: utf-8 -*-
"""
Created on Thu May 31 10:55:15 2018

@author: Dell
"""
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("Foodtruck.csv") 

features=df.iloc[:,:-1].values#set of independent datasets
label=df.iloc[:,-1].values#set of dependent datasets

from sklearn.model_selection import train_test_split
features_train,features_test,label_train,label_test=train_test_split(features,label,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(features_train,label_train)

label_pred=regressor.predict(features_test)

score=regressor.score(features_test,label_test)

print regressor.predict(3.073)

plt.scatter(features_train,label_train,color="red")
plt.plot(features_train,regressor.predict(features_train),color="blue")
plt.title("population versus profit (training set)")
plt.xlabel("population")
plt.ylabel("profit")
plt.show()

plt.scatter(features_test,label_test,color="red")
plt.plot(features_train,regressor.predict(features_train),color="blue")
plt.title("population versus profit (training set)")
plt.xlabel("population")
plt.ylabel("profit")
plt.show()
