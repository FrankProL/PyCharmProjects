#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/4/3 16:16
# @Author  : Frank
# @Site    : 
# @File    : insert_sort.py
# @Software: PyCharm
"""
"""插入排序
    将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
    从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。（如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）
"""
import random


def insert_sort(arr):
    for i in range(len(arr)):       # 从第一个元素开始，将第i个元素插入前面已经排好序列的合适位置（将这个元素和前面的元素，从后向前一个一个比较，直到找到合适的位置）
        preindex = i - 1                            # 指向前一个位置
        current = arr[i]                            # current 记录arr[i]当前值
        while preindex >= 0 and arr[preindex] > current:    # preindex索引位置大于等于0，且大于记录下的a[i]值时
            arr[preindex + 1] = arr[preindex]               # 将a[i]的值替换为前面已经排好序的最后一个值（即排序好的最大值a[i-1]）
            preindex -= 1                                   # 索引继续向前一个位置，循环判断，将比a[i]大的值不断向后替换，直到前一个值不大于a[i]，循环结束
        arr[preindex + 1] = current                         # 此时索引处的值<=a[i],preindex+1处的值大于a[i],已被替换到后一个位置，将a[i]的值放到preindex处
    return arr


if __name__ == '__main__':
    data = [random.randint(1, 100) for i in range(10)]
    print insert_sort(data)
