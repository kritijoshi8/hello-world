# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 11:39:47 2018

@author: Dell
"""

import pandas as pd
df=pd.read_csv('breast_cancer.csv')

df.iloc[:,:]=df.apply(lambda x:x.fillna(x.value_counts().index[0])) 
features=df.iloc[:,1:-1].values
labels=df.iloc[:,-1:].values



from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0,)


from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf', random_state = 0)
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

print 'score:', classifier.score(features_test,labels_test)

print 'Predicting whether a women has Benign tumor or Malignant tumor',classifier.predict([[6,2,5,3,2,7,9,2,4]])