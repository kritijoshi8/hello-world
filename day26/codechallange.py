# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 12:06:25 2018

@author: Dell
"""

import pandas as pd

df=pd.read_csv('movie.csv')

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
for i in range(0, 2000):
    text = re.sub('[^a-zA-Z]', ' ', df['text'][i])
    text = text.lower()
    text = text.split()
    ps = PorterStemmer()
    text = [ps.stem(word) for word in text if not word in set(stopwords.words('english'))]
    text = ' '.join(text)
    corpus.append(text) 
    
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 2000)
features = cv.fit_transform(corpus).toarray()
labels = df.iloc[:, 0].values

from sklearn.preprocessing import LabelEncoder
labelencoder=LabelEncoder()
labels=labelencoder.fit_transform(labels)

 
