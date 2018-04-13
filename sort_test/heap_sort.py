#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/4/4 14:57
# @Author  : Frank
# @Site    : 
# @File    : heap_sort.py
# @Software: PyCharm
"""
"""堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。
    堆排序可以说是一种利用堆的概念来排序的选择排序
    1.将长度为n的待排序的数组进行堆有序化构造成一个大顶堆
        初始化大顶堆(从最后一个有子节点开始往上调整最大堆)
    2.将根节点与尾节点交换并输出此时的尾节点
        堆顶元素与最后一个元素交换，交换后堆长度减一。
        交换之后可能造成被交换的孩子节点不满足堆的性质，因此每次交换之后要重新对被交换的孩子节点进行调整
        堆顶元素(最大数)与堆最后一个数交换后，需再次调整成大顶堆，此时是从上往下调整的。
    3.将剩余的n -1个节点重新进行堆有序化
    4.重复步骤2，步骤3直至构造成一个有序序列
    详细图解补充，见github
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
