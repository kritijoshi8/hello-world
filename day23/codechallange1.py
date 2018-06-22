# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 11:23:24 2018

@author: Dell
"""

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("crime_data.csv") 

features=df.iloc[:,[1,2,4]].values

from sklearn.decomposition import PCA
pca=PCA(n_components=2)
features=pca.fit_transform(features)
explained_variance=pca.explained_variance_ratio_

from sklearn.cluster import KMeans
kmeans=KMeans(n_clusters=3,init='k-means++',random_state=0)
y_kmeans=kmeans.fit_predict(features)

plt.scatter(features[y_kmeans==0,0],features[y_kmeans==0,1],s=100,c='red',label='murder')
plt.scatter(features[y_kmeans==1,0],features[y_kmeans==1,1],s=100,c='blue',label='assault')
plt.scatter(features[y_kmeans==2,0],features[y_kmeans==2,1],s=100,c='green',label='rape')
plt.title('clusters of crime')
plt.xlabel('crime')
plt.ylabel('cities')
plt.legend()
plt.show()
