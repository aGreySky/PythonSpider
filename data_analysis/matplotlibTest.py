# -*- coding:utf-8 -*-
"""
@author:aGreysky
@file:matplotlibTest.py
@time:2018/5/7 14:32
"""
import numpy as np
import matplotlib.pyplot as plt
def main():

    '''
    #横轴[-pi,pi]之间，256个点，不包含端点
    x = np.linspace(-np.pi,np.pi,256,endpoint=True)
    #定义cos，sin
    c,s=np.cos(x),np.sin(x)
    #图一
    plt.figure(1)
    #绘制自变量x，因变量c ，color颜色，linewidth：线宽，指定label名
    plt.plot(x,c,color="blue",linewidth=1.0,linestyle="-",label="COS",alpha=0.5)
    # 绘制自变量x，因变量s，线形为*，指定label名
    plt.plot(x,s,"r*",label="SIN")
    #标题
    plt.title("COS & SIN")
    #编辑器
    ax=plt.gca()
    #spines为边线，隐藏right，top，把left，bottom放在坐标0处
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    ax.spines["left"].set_position(("data",0))
    ax.spines["bottom"].set_position(("data", 0))
    #坐标设在x轴下，y轴左边
    ax.xaxis.set_ticks_position("bottom")
    ax.yaxis.set_ticks_position("left")
    #横轴标记位置
    plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],
               [r'$-\pi$',r'$-\pi/2$',r'$+\pi/2$',r'$+\pi$',])
    # y轴标记位置，[-1,1]中的5个点
    plt.yticks(np.linspace(-1,1,5,endpoint=True))
    for label in ax.get_xticklabels()+ax.get_yticklabels():
        label.set_fontsize(16)
        #设置数字
        label.set_bbox(dict(facecolor="white", edgecolor="None", alpha=0.2))
    #注释左上角
    plt.legend(loc="upper left")
    #网格线
    plt.grid()
    #坐标范围，前2为x轴，后2为y轴
    #plt.axis([-1,1,-0.5,1])
    #填充指定区域颜色
    plt.fill_between(x,np.abs(x)<0.5,c,c>0.5,color="green",alpha=0.25)
    #为x=1作虚线
    t=1
    plt.plot([t,t],[0,np.cos(t)],"y",linewidth=3,linestyle="--")
    #（cos（1））加注释
    plt.annotate("cos(1)",xy=(t,np.cos(1)),xycoords="data",xytext=(+10,+30),
                 textcoords="offset points",arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2"))

    '''

    #scatter散点图
    #图表
    fig=plt.figure()
    #3行3列
    ax=fig.add_subplot(3,3,1)
    n=128
    #随机数
    X=np.random.normal(0,1,n)
    Y=np.random.normal(0,1,n)
    #颜色范围
    T=np.arctan2(Y,X)
    # plt.axes([0.025,0.025,0.95,0.95])
    #s点的大小，c点的颜色，alpha透明度
    ax.scatter(X,Y,s=75,c=T,alpha=.5)
    #xy的范围
    plt.xlim(-1.5,1.5),plt.xticks([])
    plt.ylim(-1.5, 1.5), plt.yticks([])
    plt.axis()
    plt.title("scatter")

    #bar柱状图
    ax=fig.add_subplot(332)
    n=10
    #0~9数列
    X=np.arange(n)
    #Y1,Y2随机数
    Y1=(1-X/float(n))*np.random.uniform(0.5,1.0,n)
    Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
    #注释位置颜色
    ax.bar(X,+Y1,facecolor='#9999ff',edgecolor='white')
    ax.bar(X,-Y2,facecolor='#ff9999',edgecolor='white')
    for x,y in zip(X,Y1):
        plt.text(x+4,y+0.05,'%.2f' %y,ha='center',va='top')
    for x,y in zip(X,Y2):
        plt.text(x+4,-y-0.05,'%.2f' %y,ha='center',va='top')


    #Pie饼图
    fig.add_subplot(333)
    #20个区域
    n=20
    Z=np.ones(n)
    Z[-1]*=2
    #explode离中心的距离
    plt.pie(Z,explode=Z*.05,colors=['%f'%(i/float(n)) for i in range(n)],
            labels=['%.2f'%(i/float(n)) for i in range(n)])
    plt.gca().set_aspect('equal')
    plt.xticks([]),plt.yticks([])

    #polar极坐标
    fig.add_subplot(334,polar=True)
    n=20
    theta=np.arange(0.0,2*np.pi,2*np.pi/n)
    radii=10*np.random.rand(n)
    plt.polar(theta, radii)
    # plt.plot(theta,radii)

    #heatmap热图
    fig.add_subplot(335)
    #cm上色
    from  matplotlib import cm
    data = np.random.rand(3,3)
    cmap = cm.Blues
    map = plt.imshow(data,interpolation='nearest',cmap=cmap,aspect='auto',vmin=0,vmax=1)

    #3D
    from mpl_toolkits.mplot3d import Axes3D
    ax = fig.add_subplot(336,projection="3d")
    ax.scatter(1,1,3,s=100)

    #hot map 热力图
    fig.add_subplot(313)
    def f(x,y):
        return (1-x/2+x **5 +y **3) * np.exp(-x **2 - y ** 2)
    n = 256
    x = np.linspace(-3,3,n)
    y = np.linspace(-3,3,n)
    X,Y = np.meshgrid(x,y)
    plt.contourf(X,Y,f(X,Y),8,alpha=.75,cmap=plt.cm.hot)

    plt.savefig("./data/fig.png")
    plt.show()



if __name__ == '__main__':
    main()