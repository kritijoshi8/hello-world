# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 11:59:01 2018

@author: Dell
"""

import pandas as pd

df=pd.read_csv("tree_addhealth.csv") 

df=df.apply(lambda x:x.fillna(x.value_counts().index[0]))


#for 1st problem
features=df.iloc[:,[0,1,2,3,4,5,6,8,9,10,11,12,13,14,15]].values
labels=df.iloc[:,7].values

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0) 

from sklearn.tree import DecisionTreeClassifier
classifier=DecisionTreeClassifier(criterion='entropy',random_state=0)
classifier.fit(features_train,labels_train)

labels_pred=classifier.predict(features_test)
print classifier.score(features_test,labels_test) 

#for 2nd problem
features1=df.iloc[:,[0,16]].values
labels1=df.iloc[:,-4].values

from sklearn.model_selection import train_test_split
features1_train,features1_test,labels1_train,labels1_test=train_test_split(features1,labels1,test_size=0.2,random_state=0) 

from sklearn.tree import DecisionTreeClassifier
classifier=DecisionTreeClassifier(criterion='entropy',random_state=0)
classifier.fit(features_train,labels_train)

labels_pred=classifier.predict(features_test)
print classifier.score(features_test,labels_test) 









