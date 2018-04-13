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
    算法步骤
        1.从数列中挑出一个元素，称为 “基准”（pivot）;
        2.重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
        在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
        3.递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序；
    递归的最底部情形，是数列的大小是零或一，也就是永远都已经被排序好了。虽然一直递归下去，但是这个算法总会退出，
    因为在每次的迭代（iteration）中，它至少会把一个元素摆到它最后的位置去。
"""
import random


def quick_sort(arr, left=None, right=None):
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(arr) - 1 if not isinstance(right, (int, float)) else right
    if left < right:
        partionIndex=partition(arr,left,right)  # 小于基准值的元素数，即左侧元素数
        quick_sort(arr,left,partionIndex-1)     # 对左侧元素递归使用快排
        quick_sort(arr,partionIndex+1,right)    # 对右侧元素递归使用快排
    return arr


def partition(arr, left, right):
    pivot = left                    # 选取最左侧元素作为基准
    index = pivot + 1               # index指向分区位置，index左侧是小于基准的元素
    i = index
    while i <= right:
        if arr[i] < arr[pivot]:     # 遍历元素，如果元素小于基准值，就将元素和当前的分区位置元素交换，并将分区位置右移，（将较小的元素移到左侧）
            swap(arr, i, index)
            index += 1
        i += 1
    swap(arr,pivot,index-1)         # 将基准交换到分区位置
    return index - 1                # 返回的是小于基准的元素数


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    data=[random.randint(1,100) for i in range(1,10)]
    print data
    print quick_sort(data)
