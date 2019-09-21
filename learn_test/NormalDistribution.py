#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/8/18 11:23
# @Author  : Frank
# @Site    : 
# @File    : NormalDistribution.py
# @Software: PyCharm
产生符合正态分布的数
http://note.youdao.com/noteshare?id=ed0e03663bc744a77c047936a50a4e55&sub=145418F476514932B949A86C39662C00
"""
import numpy as np
from scipy.special import erfinv

def boxmullersampling(mu=0,sigma=1,size=1):     # mu期望，sigma方差
    u=np.random.uniform(size=size)
    v=np.random.uniform(size=size)
    z=np.sqrt(-2*np.log(u))*np.cos(2*np.pi*v)
    return mu+sigma*z

def inverfsampling(mu=0,sigma=1,size=1):
    z=np.sqrt(2)*erfinv(2*np.random.uniform(size=size)-1)
    return mu+sigma*z

def test():
    '''
    简单生成正态分布的代码：x = numpy.round(numpy.random.normal(1，1，10),2)。
    其中numpy.random.normal的三个参数代表符合X~N（1，1）的正态分布抽样10次。
    ep：假设有5000个学生，他们的身高和体重分别符合X~N（1.75，0.2）和Y~N（100，10）的正态分布，
    那么通过以下代码简单实现均值、中位数、相关系数和标准差的分析。
    '''
    # 生成正态分布
    x = np.round(np.random.normal(1.75, 0.2, 5000), 2)
    y = np.round(np.random.normal(100, 10, 5000), 2)
    # 使成为二维数组
    z = np.column_stack((x, y))
    print(z)
    # 输出身高均值（输出体重均值只需将0改为1）
    print(np.mean(z[:, 0]))
    # 输出身高中位数
    print(np.median(z[:, 0]))
    # 输出两组数据相关系数
    print(np.corrcoef(z[:, 0], z[:, 1]))
    # 输出身高标准差
    print(np.std(z[:, 0]))

if __name__ == '__main__':
    print(boxmullersampling(0,1,1))
    print(inverfsampling(0,1,1))
    test()
