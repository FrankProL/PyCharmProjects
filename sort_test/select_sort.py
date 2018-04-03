#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/4/3 15:00
# @Author  : Frank
# @Site    : 
# @File    : select_sort.py
# @Software: PyCharm
"""
"""选择排序
    首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置
    再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
    重复第二步，直到所有元素均排序完毕。
"""
import random


def select_sort(arr):
    for j in range(0, len(arr)):
        tmp = arr[j]
        for i in range(j + 1, len(arr)):
            if arr[i] < tmp:
                tmp = arr[i]
                arr[j], arr[i] = arr[i], arr[j]
    return arr


if __name__ == '__main__':
    data = [random.randint(0, 100) for i in range(10)]
    print data
    print select_sort(data)
