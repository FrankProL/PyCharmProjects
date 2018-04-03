#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/4/3 18:37
# @Author  : Frank
# @Site    : 
# @File    : merge_sort.py
# @Software: PyCharm
"""
"""归并排序
    归并排序
    归并排序（Merge sort）是建立在归并操作上的一种有效的排序算法。该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。
    和选择排序一样，归并排序的性能不受输入数据的影响，但表现比选择排序好的多，因为始终都是 O(nlogn) 的时间复杂度。代价是需要额外的内存空间。

    作为一种典型的分而治之思想的算法应用，归并排序的实现由两种方法：
        1.自上而下的递归（所有递归的方法都可以用迭代重写，所以就有了第 2 种方法）；
        2.自下而上的迭代；
"""
import math
import random


def merge_sort(arr):
    if (len(arr) < 2):
        return arr
    middle = int(math.floor(len(arr) / 2))
    left, right = arr[0:middle], arr[middle:]
    return merge(merge_sort(left),merge_sort(right))


def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result

if __name__ == '__main__':
    data=[random.randint(1,100) for i in range(1,10)]
    print data
    print merge_sort(data)