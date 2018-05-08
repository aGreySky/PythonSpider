# -*- coding:utf-8 -*-
"""
@author:aGreysky
@file:scipyTest.py
@time:2018/5/7 20:29
"""
import numpy as np
from pylab import *
def main():
    #1--Integral积分
    from scipy.integrate import quad,dblquad,nquad
    #函数exp(-x)从0到无穷大的积分值，结果包含估计值和误差
    print(quad(lambda x:np.exp(-x),0,np.inf))
    #dblquad二元积分，函数e的-x*t/t3，t取0~无穷大，x取t的函数
    print(dblquad(lambda t,x:np.exp(-x*t)/t**3,0,np.inf,lambda x:1,lambda x:np.inf))
    def f(x,y):
        return x*y
    def bound_y():
        return [0,0.5]
    def bound_x(y):
        return [0,1-2*y]
    print(nquad(f,[bound_x,bound_y]))

    #2-Optimizer最优控制器
    from scipy.optimize import minimize
    def rosen(x):
        return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0+(1-x[:-1])**2.0)
    x0=np.array([1.3,0.7,0.8,1.9,1.2])
    #计算最小值  xtol精度
    res=minimize(rosen,x0,method="nelder-mead",options={"xtol":1e-8,"disp":True})
    print("ROSE MINI:",res.x)

    def fun(x):
        return (2*x[0]*x[1]+2*x[0]-x[0]**2-2*x[1]**2)
    #偏导数
    def func_deriv(x):
        dfdx0 = (-2*x[0]+2*x[1]+2)
        dfdx1 = (2*x[0]-4*x[1])
        return np.array([dfdx0,dfdx1])

    #3--Interpolation插值
    x=np.linspace(0,1,10)
    y=np.sin(2*np.pi*x)
    from scipy.interpolate import interp1d
    li=interp1d(x,y,kind="cubic")
    x_new=np.linspace(0,1,50)
    y_new=li(x_new)
    figure()
    plot(x,y,"r")
    plot(x_new,y_new,"k")
    show()
    print(y_new)

    #4-Linear线性函数
    from scipy import linalg as lg
    arr=np.array([[1,2],[3,4]])
    #行列式
    print("det:",lg.det(arr))
    #逆矩阵
    print("Inv:",lg.inv(arr))
    #解线性方程组
    b=np.array([6,14])
    print("sol:",lg.solve(arr,b))
    #特殊值
    print("eig:",lg.eig(arr))
    #矩阵分解LU,QR,SVD,schur
    print("LU:",lg.lu(arr))
    print("QR:",lg.qr(arr))
    print("svd:",lg.svd(arr))
    print("schur:",lg.schur(arr))





if __name__ == '__main__':
    main()