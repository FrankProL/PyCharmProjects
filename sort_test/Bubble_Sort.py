#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/4/3 11:31
# @Author  : Frank
# @Site    : 
# @File    : Bubble_Sort.py
# @Software: PyCharm
"""

import random

def bubble_sort(arr):
    # for j in range(1,len(arr)):
    #     for i in range(0,len(arr)-j):
    #         if arr[i]>arr[i+1]:
    #             arr[i],arr[i+1]=arr[i+1],arr[i]
    for i in range(0,len(arr)):             # 外层循环控制冒泡的趟数
        for j in range(0,len(arr)-1-i):     # 内层控制每一趟从头冒泡的尾，每趟末尾都是之前冒泡的结果，可以不用再比较
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

if __name__ == '__main__':
    data = [random.randint(1, 100) for i in range(10)]
    print data
    print bubble_sort(data)