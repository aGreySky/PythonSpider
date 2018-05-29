#-*- coding=utf-8 -*-
"""
@author: aGreySky
"""
import pandas as pd
import matplotlib.pyplot as plt
def main():
    weather = pd.read_csv('./data/weather.csv', encoding='gb2312')
    plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
    plt.xlabel("日期/天")
    plt.ylabel("温度/°C")
    plt.plot(weather[u'日期'], weather[u'白天温度/°C'])
    plt.plot(weather[u'日期'], weather[u'夜间温度/°C'], c='green')
    plt.legend(loc='best')
    print(weather[u'城市'][0])
    plt.title(weather[u'城市'][0] + "未来天气图")
    plt.savefig("./data/analysis.png")
    plt.show()

if __name__ == '__main__':
    main()