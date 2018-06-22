 # -*- coding: utf-8 -*-
"""
Created on Wed May 30 11:57:41 2018

@author: Dell
"""

import pandas as pd
df=pd.read_csv('Red_Wine.csv')

df=df.apply(lambda x:x.fillna(x.value_counts().index[0]))


features=df.iloc[:,0:-1].values
labels=df.iloc[:,-1].values


from sklearn.preprocessing import LabelEncoder,OneHotEncoder,StandardScaler
#label_encoding
labelencoder=LabelEncoder()
features[:,0]=labelencoder.fit_transform(features[:,0])

#one_hot_encoding
onehotencoder=OneHotEncoder(categorical_features=[0])
features=onehotencoder.fit_transform(features).toarray()

#feature_scaling
sc=StandardScaler()
features=sc.fit_transform(features)


from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)


view = pd.DataFrame(features)




















