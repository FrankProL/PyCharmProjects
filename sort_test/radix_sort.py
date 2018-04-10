#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/4/9 17:14
# @Author  : Frank
# @Site    : 
# @File    : radix_sort.py
# @Software: PyCharm
"""
import random

"""基数排序是一种非比较型整数排序算法，
    其原理是将整数按位数切割成不同的数字，然后按每个位数分别比较。
    由于整数也可以表达字符串（比如名字或日期）和特定格式的浮点数，所以基数排序也不是只能使用于整数。
    基数排序有两种方法：
        LSD（Least significant digital）或MSD（Most significant digital），
        LSD的排序方式由键值的最右边开始，而MSD则相反，由键值的最左边开始
    
    基数排序 vs 计数排序 vs 桶排序
        这三种排序算法都利用了桶的概念，但对桶的使用方法上有明显差异：
            基数排序：根据键值的每位数字来分配桶；
            计数排序：每个桶只存储单一键值；
            桶排序：每个桶存储一定范围的数值；
"""


def radix_sort(arr):
    maxsize = len(str(max(arr)))
    for k in xrange(maxsize):  # k轮排序， 最多几位数，就进行几轮桶排序
        bucket = [[] for i in xrange(10)]
        for i in arr:
            bucket[i / (10 ** k) % 10].append(i)  # 析取整数第K位数字 （从低到高）
        arr = [a for b in bucket for a in b]  # 直到最大数的最高位也被添加到桶中，或者说，当所有的元素都被被在第 0 个桶中，基数排序就结束了
    return arr


# def sort(a, radix=10):
#     """a为整数列表， radix为基数"""
#     K = int(math.ceil(math.log(max(a), radix)))  # 用K位数可表示任意整数
#     bucket = [[] for i in range(radix)]  # 不能用 [[]]*radix
#     for i in range(1, K + 1):  # K次循环
#         for val in a:
#             bucket[val % (radix ** i) / (radix ** (i - 1))].append(val)  # 析取整数第K位数字 （从低到高）
#         del a[:]
#         for each in bucket:
#             a.extend(each)  # 桶合并
#         bucket = [[] for i in range(radix)]

if __name__ == '__main__':
    data = [random.randint(1, 5) for i in range(10)]
    print data
    print radix_sort(data)


# """求数字的最高位"""
# i = 9258900000
# if i >= 100000000:
#     i /= 100000000
# if i >= 10000:
#     i /= 10000
# if i >= 100:
#     i /= 100
# if i >= 10:
#     i /= 10
# print i
#
# number = 839040000000000000000000
# while number >= 10:
#     number /= 10
# print number
