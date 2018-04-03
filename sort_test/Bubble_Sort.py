#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/4/3 11:31
# @Author  : Frank
# @Site    : 
# @File    : Bubble_Sort.py
# @Software: PyCharm
"""
"""冒泡排序"""
import random

def bubble_sort(arr):
    for j in range(1,len(arr)):
        for i in range(0,len(arr)-j):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
    return arr

if __name__ == '__main__':
    data = [random.randint(1, 100) for i in range(10)]
    print data
    print bubble_sort(data)