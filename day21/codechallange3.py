# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 14:04:02 2018

@author: Dell
"""

import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('tshirts.csv')

features=df.iloc[:,1:].values

from sklearn.cluster import KMeans
wcss=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i,init='k-means++',random_state=0)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11),wcss)
plt.title('The elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()


kmeans=KMeans(n_clusters=3,init='k-means++',random_state=0)
y_kmeans=kmeans.fit_predict(features)

plt.scatter(features[y_kmeans==0,0],features[y_kmeans==0,1],s=100,c='red',label='cluster1')
plt.scatter(features[y_kmeans==1,0],features[y_kmeans==1,1],s=100,c='blue',label='cluster2')
plt.scatter(features[y_kmeans==2,0],features[y_kmeans==2,1],s=100,c='green',label='cluster3')
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=300,c='yellow',label='centroids')
plt.title('clusters of delivery')
plt.xlabel('height')
plt.ylabel('weight')
plt.show()
