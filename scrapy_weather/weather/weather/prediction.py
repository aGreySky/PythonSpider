#-*- coding=utf-8 -*-
"""
@author: aGreySky
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn
from sklearn.linear_model import LinearRegression




def main():
    weather = pd.read_csv('./data/weather.csv', encoding='gb2312')
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签

    # 图表
    fig = plt.figure()


    # 1行2列
    ax1 = fig.add_subplot(1, 2, 1)
    # 标题
    plt.title(weather[u'城市'][0] + '未来几天温度规律(线性回归)')
    #根据数据长度确定x取值
    x = np.arange(1, len(weather[u"白天温度/°C"])+1, 1)
    ax1.scatter(x, weather[u"白天温度/°C"])
    plt.xlabel('未来天数/天')
    plt.ylabel('温度/°C')

    # 线性回归实现白天温度 & 日期 关系
    lr = LinearRegression(fit_intercept=True)
    lr.fit(x.reshape(7, -1), weather[u"白天温度/°C"])
    predictions = lr.predict(x.reshape(7, -1))
    ax1.plot(x, predictions, c='blue')


    # 根据数据长度确定x取值
    x = np.arange(1, len(weather[u"夜间温度/°C"]) + 1, 1)
    ax1.scatter(x, weather[u"夜间温度/°C"])

    # 线性回归实现夜间温度 & 日期 关系
    lr = LinearRegression(fit_intercept=True)
    lr.fit(x.reshape(7, -1), weather[u"夜间温度/°C"])
    predictions = lr.predict(x.reshape(7, -1))
    ax1.plot(x, predictions, c='red')
    plt.legend(loc='best')

    # 逻辑回归实现白天温度 & 日期关系
    ax2 = fig.add_subplot(1, 2, 2)
    plt.title(weather[u'城市'][0] + '未来几天温度规律(逻辑回归)')

    # y轴表示可能性
    plt.xlabel('温度/°C')
    plt.ylabel("Probability(可能性)")

    # 逻辑回归
    from sklearn.linear_model import LogisticRegression
    logistic_model = LogisticRegression()

    # 将前3条数据作为训练集，后面的作为测试集
    num_train = 3
    data_train = weather[:num_train]
    data_test = weather[num_train:]
    # 训练数据
    logistic_model.fit(data_train[[u"白天温度/°C"]].astype('int'),
                       np.arange(1, len(data_train[u"白天温度/°C"]) + 1).astype('int'))
    pred_probs = logistic_model.predict_proba(data_test[[u"白天温度/°C"]].astype('int'))
    # 因为predict_proba返回的是一个两列的矩阵，
    # 矩阵的每一行代表的是对一个事件的预测结果，
    # 第一列代表该事件不会发生的概率，
    # 第二列代表的是该事件会发生的概率。
    # 而这里需要的是第二列的数据
    plt.scatter(data_test[u"白天温度/°C"], pred_probs[:, 1])

    # 逻辑回归实现夜晚温度 & 日期关系

    # 逻辑回归
    from sklearn.linear_model import LogisticRegression
    logistic_model = LogisticRegression()

    # 将前3条数据作为训练集，后面的作为测试集
    num_train = 3
    data_train = weather[:num_train]
    data_test = weather[num_train:]
    # 训练数据
    logistic_model.fit(data_train[[u"夜间温度/°C"]].astype('int'), np.arange(1, len(data_train[u"夜间温度/°C"])+1).astype('int'))
    pred_probs = logistic_model.predict_proba(data_test[[u"夜间温度/°C"]].astype('int'))
    # 因为predict_proba返回的是一个两列的矩阵，
    # 矩阵的每一行代表的是对一个事件的预测结果，
    # 第一列代表该事件不会发生的概率，
    # 第二列代表的是该事件会发生的概率。
    # 而这里需要的是第二列的数据
    plt.scatter(data_test[u"夜间温度/°C"], pred_probs[:, 1])

    plt.savefig("./data/prediction.png")
    plt.show()




if __name__ == '__main__':
    main()