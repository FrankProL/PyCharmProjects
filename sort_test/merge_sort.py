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
        1.自上而下的递归（所有递归的方法都可以用迭代重写，所以就有了第 2 种方法）；            递归，函数自己调用自己，把一个大型的复杂的问题转化为一个与原问题相似的规模较小的问题来解决,可以极大的减少代码量
        2.自下而上的迭代；                                                                      迭代，明确递推关系，不断重复
"""
import math
import random


def merge_sort(arr):                    # 采用递归调用方式，思路简单，代码清晰，大问题转化为小问题
    if len(arr) < 2:
        return arr
    middle = int(math.floor(len(arr) / 2))
    left, right = arr[0:middle], arr[middle:]
    return merge(merge_sort(left), merge_sort(right))


def merge_sort_2(arr):                  # 采用迭代实现，需要考虑清晰迭代的步骤
    arr_len = len(arr)
    if arr_len < 2:
        return arr
    size = 1
    while size <= arr_len - 1:
        left = 0
        while left + size <= arr_len - 1:
            mid = left + size - 1
            right = mid + size
            if right > arr_len - 1:
                right = arr_len - 1
            result = merge(arr[left:mid + 1], arr[(mid + 1):( right + 1)])
            arr[left:right + 1] = result
            left=right+1
        size *= 2
    return arr


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
    data = [random.randint(-11, 1000) for i in range(1, 1000)]
    print data
    print merge_sort_2(data)
    # import profile                        # profile 测试函数性能
    # profile.run("merge_sort(data)")
    # profile.run('merge_sort_2(data)')
