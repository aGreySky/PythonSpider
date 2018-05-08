# -*- coding:utf-8 -*-
"""
@author:aGreysky
@file:numpy_test.py
@time:2018/5/316:39
"""
import numpy as np
from numpy.linalg import *

def main():
    lst=[[1,3,5],[2,4,6]]
    print(type(lst))
    np_lst=np.array(lst)
    print(type(np_lst))
    np_lst=np.array(lst,dtype=np.float)
    #bool,int,int8,int16,int32,....
    print(np_lst.shape)
    print(np_lst.ndim)
    print(np_lst.dtype)
    print(np_lst.itemsize)
    print(np_lst.size)
    #2 Some Arrays
    print(np.zeros([2,4]))
    print(np.ones([3,5]))
    print("Rand:")
    print(np.random.rand(2,4))
    print(np.random.rand())
    print("RandInt:")
    print(np.random.randint(1,10,3))
    print("Randn:")
    print(np.random.randn(2,4))
    print("Choice:")
    print(np.random.choice([10,20,30,2,8]))
    print("Distribute:")
    print(np.random.beta(2,4,1))
    #3 Array Opes
    print(np.arange(1,11).reshape([2,-1]))
    print("Exp")
    print(np.exp(lst))
    print("Exp2")
    print(np.exp2(lst))
    print("Sqrt")
    print(np.sqrt(lst))
    print("Sin")
    print(np.sin(lst))
    print("Log")
    print(np.log(lst))

    lst = np.array([[[1,2,3,4],
                     [4,5,6,7]],
                    [[7,8,9,10],[10,11,12,13]],
                    [[14,15,16,17],[18,19,20,21]]
                    ])
    print("sum")
    print(lst.sum(axis=1))
    print("max")
    print(lst.max(axis=1))
    print("min")
    print(lst.min(axis=0))
    lst1 = np.array([10, 20, 30, 40])
    lst2=np.array([4,3,2,1])
    print("add")
    print(lst1+lst2)
    print("sub")
    print(lst1-lst2)
    print("mul")
    print(lst1-lst2)
    print("div")
    print(lst1/lst2)
    print("square")
    print(lst1**2)
    print("dot")
    print(np.dot(lst1.reshape([2,2]),lst2.reshape([2,2])))

    #4 liner

    print(np.eye(3))
    lst = np.array([[1.,2.],
                   [3.,4.]])
    print("inv")
    print(inv(lst))
    print("T")
    print(lst.transpose())



if __name__ == '__main__':
    main()
