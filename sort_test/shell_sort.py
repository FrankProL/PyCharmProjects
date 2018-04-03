#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/4/3 16:42
# @Author  : Frank
# @Site    : 
# @File    : shell_sort.py
# @Software: PyCharm
"""
"""希尔排序
    希尔排序是基于插入排序的以下两点性质而提出改进方法的：
        1.插入排序在对几乎已经排好序的数据操作时，效率高，即可以达到线性排序的效率；
        2.但插入排序一般来说是低效的，因为插入排序每次只能将数据移动一位；
    希尔排序的基本思想是：先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，待整个序列中的记录“基本有序”时，再对全体记录进行依次直接插入排序。
    https://www.cnblogs.com/chengxiao/p/6104371.html
    https://blog.csdn.net/jianfpeng241241/article/details/51707618
"""
import math
import random


def shell_sort(arr):
    gap = 1
    while (gap < len(arr) / 3):
        gap = gap * 3 + 1
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i - gap
            while j >= 0 and arr[j] > temp:
                arr[j + gap] = arr[j]
                j -= gap
            arr[j + gap] = temp
        gap = int(math.floor(gap / 3))
    return arr


if __name__ == '__main__':
    data = [random.randint(1, 100) for i in range(10)]
    print data
    print shell_sort(data)
