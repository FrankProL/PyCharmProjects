#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/4/12 15:23
# @Author  : Frank
# @Site    : 
# @File    : tanxinsuanfa.py
# @Software: PyCharm
"""
import random

"""贪心算法求解调度问题
    总完成时间为从任务提交开始到结束的时间，包括了任务的等待时间
"""
def tanxin(task):
    task.sort()  # list.sort()对自身排序，无返回值
    # print (sorted(task))     # sorted() 内置函数，返回一个有序的新列表，原列表不变
    sum = 0
    for i, time in enumerate(task):
        sum += time * (len(task) - i)
    return sum, task


if __name__ == '__main__':
    task = [random.randint(1, 100) for i in range(1, 10)]
    time, l = tanxin(task)
    print ('贪心调度方式的总时间：')
    print (time)
    print ('贪心任务序列：')
    print (l)




