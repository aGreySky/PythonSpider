# -*- coding:utf-8 -*-
"""
@author:aGreysky
@file:main.py
@time:2018/5/8 13:40
"""
def main():
    import pandas as pd
    import matplotlib.pyplot as plt
    #参数列表
    columns = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model year", "origin",
               "car name"]
    #读取数据
    f=open('E:/Python/Python爬虫/scientific_calculation/data/auto-mpg.data')
    cars = pd.read_table(f,delim_whitespace=True, names=columns)
    #打印前五行
    #print(cars.head(5))
    #图表
    fig = plt.figure()


    #线性回归实现weight & mpg 关系
    #1行2列
    ax1 = fig.add_subplot(1, 2, 1)
    #标题
    plt.title('weight & mpg')
    #散点图  weight、acceleration：x轴   mpg：y轴
    cars.plot("weight", "mpg", kind='scatter', ax=ax1)

    import sklearn
    from sklearn.linear_model import LinearRegression
    lr = LinearRegression()
    lr.fit(cars[["weight"]], cars["mpg"])

    from sklearn.linear_model import LinearRegression
    lr = LinearRegression(fit_intercept=True)
    lr.fit(cars[["weight"]], cars["mpg"])
    predictions = lr.predict(cars[["weight"]])
    #打印5个预测值和实际值
    print("预测值：",predictions[0:5])
    print("实际值：\n",cars["mpg"][0:5])

    #散点颜色，预测线颜色
    ax1.scatter(cars["weight"], cars["mpg"], c='blue')
    ax1.scatter(cars["weight"], predictions, c='red')

    #线性回归
    lr = LinearRegression()
    lr.fit(cars[["weight"]], cars["mpg"])
    predictions = lr.predict(cars[["weight"]])
    from sklearn.metrics import mean_squared_error
    #均方误差
    mse = mean_squared_error(cars["mpg"], predictions)
    print("均方误差:",mse)
    #均方根误差
    rmse = mse ** (0.5)
    print("均方根误差:",rmse)




    #逻辑回归实现origin & mpg关系
    ax2 = fig.add_subplot(1, 2, 2)
    plt.title('map & origin')

    import numpy as np
    # Logit Function
    # def logit(x):
    #     # np.exp(x) raises x to the exponential power, ie e^x. e ~= 2.71828
    #     return np.exp(x) / (1 + np.exp(x))

    # Generate 50 real values, evenly spaced, between -6 and 6.
    #坐标范围
    # x = np.linspace(-6, 6, 50, dtype=float)

    # Transform each number in t using the logit function.
    #值转换为模型坐标
    # y = logit(x)

    # Plot the resulting data.
    # plt.plot(x, y)
    #y轴表示可能性
    plt.xlabel('mpg')
    plt.ylabel("Probability")

    from sklearn.linear_model import LinearRegression
    #线性回归
    linear_model = LinearRegression()
    #训练
    linear_model.fit(cars[["mpg"]], cars["origin"])

    #逻辑回归
    from sklearn.linear_model import LogisticRegression
    logistic_model = LogisticRegression()
    # 对数据集进行随机重排序
    admissions = cars.loc[np.random.permutation(cars.index)]

    # 将随机排序后的前70条数据作为训练集，后面的作为测试集
    num_train = 70
    data_train = cars[:num_train]
    data_test = cars[num_train:]
    #训练数据
    logistic_model.fit(data_train[["mpg"]].astype('int'), data_train["origin"].astype('int'))
    pred_probs = logistic_model.predict_proba(data_test[["mpg"]].astype('int'))
    # 因为predict_proba返回的是一个两列的矩阵，
    # 矩阵的每一行代表的是对一个事件的预测结果，
    # 第一列代表该事件不会发生的概率，
    # 第二列代表的是该事件会发生的概率。
    # 而这里需要的是第二列的数据
    plt.scatter(data_test["mpg"], pred_probs[:, 1])
    plt.show()

if __name__ == '__main__':
    main()

