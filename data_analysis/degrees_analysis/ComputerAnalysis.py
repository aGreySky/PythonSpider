# -*- coding:utf-8 -*-
"""
@author:aGreysky
@file:ComputerAnalysis.py
@time:2018/5/8 10:55
"""
import pandas as pd
import matplotlib.pyplot as plt

women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')
plt.plot(women_degrees['Year'], women_degrees['Computer Science'])
plt.plot(women_degrees['Year'], 100-women_degrees['Computer Science'], c='green', label='Men')
plt.legend(loc='upper right')
plt.title('Percentage of Computer Science Degrees Awarded By Gender')
plt.show()