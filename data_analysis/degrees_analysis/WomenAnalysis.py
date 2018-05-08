# -*- coding:utf-8 -*-
"""
@author:aGreysky
@file:WomenAnalysis.py
@time:2018/5/8 11:03
"""

import pandas as pd
import matplotlib.pyplot as plt

women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')
plt.figure()
keys=list(women_degrees.keys())
max=0
index=0 #记录哪个专业女生最多
mlist=list(women_degrees.apply(lambda x: x.sum()))#得到每列各自的总和
for i in range(1,len(mlist)):
    if(mlist[i]>max):
        max=mlist[i]
        index=i
key=keys[index] #平均女生比例最高的专业
plt.plot(women_degrees['Year'], women_degrees[key], c='blue', label='Women')
plt.legend(loc='upper right')
plt.title(key)
plt.show()