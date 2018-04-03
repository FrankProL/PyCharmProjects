#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/4/3 19:16
# @Author  : Frank
# @Site    : 
# @File    : quick_sort.py
# @Software: PyCharm
"""
"""快速排序
    快速排序使用分治法（Divide and conquer）策略来把一个串行（list）分为两个子串行（sub-lists）。
    快速排序又是一种分而治之思想在排序算法上的典型应用。本质上来看，快速排序应该算是在冒泡排序基础上的递归分治法。
    在平均状况下，排序 n 个项目要 Ο(nlogn) 次比较。在最坏状况下则需要 Ο(n2) 次比较，但这种状况并不常见。事实上，快速排序通常明显比其他 Ο(nlogn) 算法更快
"""
import random


def quick_sort(arr, left=None, right=None):
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(arr) - 1 if not isinstance(right, (int, float)) else right
    if left < right:
        partionIndex=partition(arr,left,right)
        quick_sort(arr,left,partionIndex-1)
        quick_sort(arr,partionIndex+1,right)
    return arr


def partition(arr, left, right):
    pivot = left
    index = pivot + 1
    i = index
    while i <= right:
        if arr[i] < arr[pivot]:
            swap(arr, i, index)
            index += 1
        i += 1
    swap(arr,pivot,index-1)
    return index - 1


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    data=[random.randint(1,100) for i in range(1,10)]
    print data
    print quick_sort(data)
