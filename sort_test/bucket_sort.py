#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/4/9 15:37
# @Author  : Frank
# @Site    : 
# @File    : bucket_sort.py
# @Software: PyCharm
"""
import random

import math

from sort_test.insert_sort import insert_sort

"""
    桶排序是计数排序的升级版。它利用了函数的映射关系，高效与否的关键就在于这个映射函数的确定。为了使桶排序更加高效，我们需要做到这两点：
        在额外空间充足的情况下，尽量增大桶的数量
        使用的映射函数能够将输入的 N 个数据尽可能均匀的分配到 K 个桶中
    同时，对于桶中元素的排序，选择何种比较排序算法对于性能的影响至关重要。

    桶排序类似于计数排序，当桶的数量大于max-min时，就相当于计数排序
    目前网上的桶排序代码序大都是计数排序
"""


def bucket_sort(arr, bucketnum):       # bucketnum 桶个数
    minvalue = arr[0]
    maxvalue = arr[0]
    for i in range(0, len(arr)):
        if (arr[i] < minvalue):
            minvalue = arr[i]       # 输入数据的最小值
        elif (arr[i] > maxvalue):
            maxvalue = arr[i]       # 输入数据的最大值
    if maxvalue==minvalue: return arr   # 最大值等于最小值，即单一值，不用排序，主要用于递归调用时，最终桶内只剩下相等元素
    bucketspan = int(math.floor((maxvalue - minvalue) / bucketnum + 1))      # 相当于桶的跨度区间
    buckets = [[] for i in range(bucketnum)]                                  # 初始化bucket个空桶

    for i in range(0, len(arr)):                                                # 利用映射函数将数据分配到各个桶中
        buckets[int(math.floor((arr[i] - minvalue) / bucketspan))].append(arr[i])
    print buckets


    arr = []
    for i in range(0, len(buckets)):
        # insert_sort(buckets[i])                         # 对每个桶内进行排序，这里调用了插入排序算法
        if len(buckets[i])>1:                             # 递归调用桶排序：当桶内元素大于1时，对桶内元素继续按桶排序
            bucket_sort(buckets[i],10)
        for j in range(0, len(buckets[i])):
            arr.append(buckets[i][j])
    return arr


if __name__ == '__main__':
    data = [random.randint(1, 100) for i in range(10)]
    print data
    print bucket_sort(data, 10)
