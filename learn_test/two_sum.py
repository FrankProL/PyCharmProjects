#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/12/7 19:08
# @Author  : Frank
# @Site    : 
# @File    : two_sum.py
# @Software: PyCharm
"""
def two_sum(value):
    arr = [2, 34, 3, 3246, 53, 13, 12, 23, 86]
    for i in arr:
        for j in arr:
            if i != j and i + j == value:
                print (arr.index(i),arr.index(j))
if __name__ == '__main__':
    two_sum(25)


