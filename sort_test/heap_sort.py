#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/4/4 14:57
# @Author  : Frank
# @Site    : 
# @File    : heap_sort.py
# @Software: PyCharm
"""
import random


def buildMaxHeap(arr):
    import math
    for i in range(int(math.floor(len(arr) / 2)), -1, -1):  # (n/2-1)~0的节点才有子节点,初始化大顶堆时 是从最后一个有子节点开始往上调整最大堆
        heapify(arr, i)


def heapify(arr, i):    # 根节点为0，结点下标为i,左孩子则为2*i+1,右孩子下标则为2*i+2
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < arrLen and arr[left] > arr[largest]:
        largest = left
    if right < arrLen and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        swap(arr, i, largest)
        heapify(arr, largest)
        print arr


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def heapSort(arr):
    global arrLen
    arrLen = len(arr)
    buildMaxHeap(arr)
    for i in range(len(arr) - 1, 0, -1):
        swap(arr, 0, i)
        arrLen -= 1
        heapify(arr, 0)
    return arr

if __name__ == '__main__':
    data=[random.randint(1,100) for i in range(10)]
    print data
    print heapSort(data)
