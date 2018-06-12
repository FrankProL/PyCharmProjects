#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/11 13:58
# @Author  : Frank
# @Site    : 
# @File    : factorial.py
# @Software: PyCharm
"""
"""递归与分治:
    阶乘函数,阶乘函数的自变量n定义域是非负整数
    斐波那契数列
    Ackerman函数，双递归函数，ackerman函数无法用非递归方式定义
"""


def factorial(n):  # n 的阶乘
    if n == 0:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):  # 斐波那契数列 第 n 位数的值   1、1、2、3、 5、 8、 13、 21 .......
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def ackerman(n, m):
    if n == 1 and m == 0:
        return 2
    if n == 0 :
        return 1
    if m==0:
        return n+2
    return ackerman(ackerman(n-1,m),m-1)


if __name__ == '__main__':
    print (factorial(5))
    print (fibonacci(7))
    print (ackerman(1,1))
