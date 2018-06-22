# -*- coding: utf-8 -*-
"""
Created on Mon Jun 04 11:25:08 2018

@author: Dell
"""


import pandas as pd
import matplotlib.pyplot as plt 

data=pd.read_csv("bluegills.csv")
features=data.iloc[:,0:1].values
labels=data.iloc[:,1].values



from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(features,labels) 

print regressor.predict(5) 
print regressor.score(features,labels)

plt.scatter(features,labels,color ="red")
plt.plot(features,regressor.predict(features),color="blue")
plt.title("graph")
plt.xlabel("length")
plt.ylabel("age")
plt.show() 

from sklearn.preprocessing import PolynomialFeatures
pol=PolynomialFeatures(degree=4)
features_pol=pol.fit_transform(features)


regressor2=LinearRegression()
regressor2.fit(features_pol,labels)
print (regressor2.predict(pol.fit_transform(5))) 

plt.scatter(features,labels,color ="red")
plt.plot(features,regressor2.predict(features_pol),color="blue")
plt.title("graph")
plt.xlabel("length")
plt.ylabel("age")
plt.show() 
print regressor2.score(features_pol,labels) 






























