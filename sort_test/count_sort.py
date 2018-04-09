#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/4/9 14:13
# @Author  : Frank
# @Site    : 
# @File    : count_sort.py
# @Software: PyCharm
"""
""" 计数排序的核心在于将输入的数据值转化为键存储在额外开辟的数组空间中。
    作为一种线性时间复杂度的排序，计数排序要求输入的数据必须是有确定范围的整数。
    
    计数排序将数据映射到额外的列表中，最好知道数据的最大最小值，这样只需要开辟一个max-min+1的列表，
    否则需要开辟一个大于等于最大值的列表（0，max+），以保证能够装下所有（min，max）的数值
    当数据中有重复值时，列表对应位置的记录+1
    
    遍历这个列表，把重复值展开就是已排序的数据
"""
import random


def countSort(arr,maxValue):
    bucketLen = maxValue + 1
    bucket = [0] * bucketLen
    sortedIndex=0
    arrLen=len(arr)
    for i in range(arrLen):
        # if not bucket[arr[i]]:
        #     bucket[arr[i]]=0
        bucket[arr[i]]+=1
    for j in range(bucketLen):
        while bucket[j]>0:
            arr[sortedIndex]=j
            sortedIndex+=1
            bucket[j]-=1
    return arr


if __name__ == '__main__':
    data=[random.randint(1,100) for i in range(10)]
    print data
    print countSort(data,100)
