# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 12:14:14 2018

@author: Dell
"""
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
iris = load_iris()
iris=iris.data 

from sklearn.decomposition import PCA
pca=PCA(n_components=2)
iris=pca.fit_transform(iris)
explained_variance=pca.explained_variance_ratio_ 

from sklearn.cluster import KMeans
kmeans=KMeans(n_clusters=3,init='k-means++',random_state=0)
y_kmeans=kmeans.fit_predict(iris)

plt.scatter(iris[y_kmeans==0,0],iris[y_kmeans==0,1],s=100,c='red',label='iris_setosa')
plt.scatter(iris[y_kmeans==1,0],iris[y_kmeans==1,1],s=100,c='blue',label='iris_versicolor')
plt.scatter(iris[y_kmeans==2,0],iris[y_kmeans==2,1],s=100,c='green',label='iris_virginica')
plt.title('clusters of flowers')
plt.xlabel('x_label')
plt.ylabel('y_label')
plt.legend()
plt.show()
