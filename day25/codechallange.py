# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 12:31:56 2018

@author: Dell
"""

import pandas as pd
#import matplotlib.pyplot as plt

df=pd.read_csv('banknotes.csv')

features=df.iloc[:,1:-1].values
labels=df.iloc[:,-1].values 

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
classifier.fit(features_train, labels_train)

labels_predict=classifier.predict(features_test)

print classifier.score(features_test,labels_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(labels_test,labels_predict)

from sklearn.model_selection import cross_val_score
accuracies=cross_val_score(estimator=classifier,X=features_train,y=labels_train,cv=10)
print ('mean accuracy is',accuracies.mean())
print (accuracies.std())




