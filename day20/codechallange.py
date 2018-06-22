# -*- coding: utf-8 -*-
"""
Created on Thu Jun 07 11:03:45 2018

@author: Dell
"""

import pandas as pd

df=pd.read_csv("mushrooms.csv") 
 
features=df.iloc[:,[5,21,22]].values
labels=df.iloc[:,0].values 

from sklearn.preprocessing import LabelEncoder
labelencoder=LabelEncoder()
for i in [0,1,2]:
    features[:,i]=labelencoder.fit_transform(features[:,i])
labels=labelencoder.fit_transform(labels)

from sklearn.preprocessing import OneHotEncoder
onehotencoder=OneHotEncoder(categorical_features=[0])
features=onehotencoder.fit_transform(features).toarray()
features=features[:,1:]
onehotencoder=OneHotEncoder(categorical_features=[9])
features=onehotencoder.fit_transform(features).toarray()
features=features[:,1:]
onehotencoder=OneHotEncoder(categorical_features=[13])
features=onehotencoder.fit_transform(features).toarray()
features=features[:,1:]

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0) 


from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=5,p=2)
classifier.fit(features_train,labels_train)

label_pred=classifier.predict(features_test) 

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(labels_test,label_pred)


print "score through classifier:",classifier.score(features_test,labels_test) 

correct=float(cm[0][0]+cm[1][1])
total=float(cm[0][0]+cm[0][1]+cm[1][0]+cm[1][1]) 

print "score through confusion_matrix:",(correct/total)


























































