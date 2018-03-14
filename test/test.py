#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/3/13 14:44
# @Author  : Frank
# @Site    : 
# @File    : test.py
# @Software: PyCharm
"""
import datetime

iter=range(10)
t=iter.__iter__()
print t.next()

print range(10).__iter__().next()

"""i 取值d[0],d[1],d[2]...
   第一次循环i=d[0]=1,然后d变为[2,3,4,5]
   第二次循环i=d[1],此时d[1]已变为3，然后列表移除3 
"""
d = [1,2,3,4,5]
for i in d:
    d.remove(i)
print d

