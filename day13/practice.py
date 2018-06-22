# -*- coding: utf-8 -*-
"""
Created on Tue May 29 10:38:16 2018

@author: Dell
"""

""" imputation-handling missing values""" 
"""textual data is categorical data"""
"""label encoding id encoding of text or 1 hot encoding"""

from sklearn.preprocessing import Imputer
imputer=Imputer(missing_values="NaN",strategy="mean",axis=0)#row_wise axis=1,column_wise axis=0
imputer=imputer.fit(features[:,1:2])#features is set od independent variables
features[:,1:2]=imputer.transform (features[:,1:2])


