# -*- coding:utf-8 -*-
"""
@author:aGreysky
@file:pandasTest.py
@time:2018/5/8 9:40
"""

import numpy as np
import pandas as pd
def main():
    #Data structure 数据结构
    s=pd.Series([i*2 for i in range(1,11)])
    #打印数据类型
    print(type(s))

    dates=pd.date_range("20180505",periods=8)
    df=pd.DataFrame(np.random.randn(8,5),index=dates,columns=list("ABCDE"))
    print(df)
if __name__ == '__main__':
    main()