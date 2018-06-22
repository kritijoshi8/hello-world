# -*- coding: utf-8 -*-
"""
Created on Fri May 25 11:47:08 2018

@author: Dell
"""

import numpy as np
import matplotlib.pyplot as plt
incomes=np.random.normal(100.0,20.0,10000)
np.mean(incomes)
np.median(incomes)
print incomes
plt.hist(incomes,50)
plt.show()
incomes1=np.append(incomes,[7000000])
print incomes1
np.mean(incomes1)
np.median(incomes1)