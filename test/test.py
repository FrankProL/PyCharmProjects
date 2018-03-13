#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/3/13 14:44
# @Author  : Frank
# @Site    : 
# @File    : test.py
# @Software: PyCharm
"""
iter=range(10)
t=iter.__iter__()
print t.next()

print range(10).__iter__().next()
