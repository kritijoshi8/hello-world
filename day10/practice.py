# -*- coding: utf-8 -*-
"""
Created on Thu May 24 10:38:06 2018

@author: Dell
"""


"""
#pandas-panal datasets
#numpy
#matplotlib
#scikitlear/sklearn 
#2-dimensional tabular data is  dataframe
"""



"""
df.head().........lists initial 5 records
df.tail().....lists bottom 5 records
df.dtypes.....datatypes of all columns
df.columns.....lists columns name
df.axes......lists row lables and column names
df.ndim.......number of dimensions
df.size.........number of rows*no. of columns
df.shape.........78,6
df.values.........represents acual values
df.describe()........concise information,average information
df.max().............maximum value in every field
df.min()...............minimum value in every field
df.mean()...............returns average value only on numerc values
df.median()...............returns central value
df.std()...............standard deviation
df.sample(10)...........returns sample values randomly from anywhere{hypothesis testing}
df.head(10).mean().......find first 10 records and calculate mean
"""


"""
df['rank']/df.rank(not allowed because of an internal command).................gives data od single column
print df['salary].mean().....mean of salary
df['salary].describe()....describes information about salary
df['salary].count()..........
df_rank=df.groupby(['rank'])
df_rank.mean()............calculates mean values group wise like for rank we have professor,associate professor and ass.professor




df_sub=df[df['salary']>120000]
df_f=df[df['sex]=='female']
df_sub.loc[10:20,['rank','sex','slary']]
df_sub.loc[10:]
df_sub.iloc[10:20,[0,3]]

df.iloc[0].........first row of data frame
df.iloc[-1]............last row of data frame
df.iloc[:,0].............first column
df.iloc[:,-1]..............last column
df.iloc[0:7]................first 7 rows
df.iloc[:,0:2]............
"""





"""
salary['phd']=salary['phd'].fillna(salary['phd'].mean())
salary=salary.fillna(salary.mean())
salary.dropna()
"""" 



























