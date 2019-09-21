#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/5/19 21:53
# @Author  : Frank
# @Site    : 
# @File    : tt.py
# @Software: PyCharm
"""

def tt(A):
    for i in A:
        print i


if __name__ == '__main__':
    A=[1,3,2,4,5]
    A.sort()

    if (A[0]>=1):
        for i in range(0,len(A)):
            print(A[i])

    for i in range(1,len(A)+1):
        pass

