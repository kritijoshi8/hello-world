# -*- coding: utf-8 -*-
"""
Created on Tue May 29 14:27:07 2018

@author: Dell
"""

import pandas as pd
df=pd.read_csv("Loan.csv",dtype={"Gender":"category","Married":"category","Dependents":"category","Education":"category","Self_Employed":"category","Property_Area":"category"})
df.dtypes 

df.Gender=df.Gender.cat.codes
df.Married=df.Married.cat.codes
df.Dependents=df.Dependents.cat.codes
df.Education=df.Education.cat.codes
df.Self_Employed=df.Self_Employed.cat.codes
df.Property_Area=df.Property_Area.cat.codes

pd.get_dummies(df, columns=['Property_Area'])








