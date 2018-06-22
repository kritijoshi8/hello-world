# -*- coding: utf-8 -*-
"""
Created on Tue May 29 11:19:12 2018

@author: Dell
"""

import pandas as pd
data=pd.read_csv("Automobile.csv") 
print data.dtypes
obj_df= data.select_dtypes(include=['object']) 

features=data.iloc[:,0:-1].values#set of independent datasets
labels=data.iloc[:,-1].values.reshape(-1,1)#set of dependent datasets
view = pd.DataFrame(features)
#data = data.apply(lambda x:x.fillna(x.value_counts().index[0]))
from sklearn.preprocessing import LabelEncoder
labelencoder=LabelEncoder()
for i in [2,3,4,5,6,7,8,14,15,17]:
    features[:,i]=labelencoder.fit_transform(features[:,i])



from sklearn.preprocessing import Imputer
imputer=Imputer(missing_values="NaN",strategy="most_frequent",axis=0)
imputer_f=imputer.fit(features[:,:])
features[:,:]=imputer_f.transform(features[:,:])

imputer_l=imputer.fit(labels)
labels=imputer_l.transform(labels)

from sklearn.preprocessing import OneHotEncoder
onehotencoder=OneHotEncoder(categorical_features=[6,7])
features=onehotencoder.fit_transform(features).toarray() 


