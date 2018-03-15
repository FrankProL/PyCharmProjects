#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/3/12 18:07
# @Author  : Frank
# @Site    : 
# @File    : onelinepy.py
# @Software: PyCharm
"""
dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print dict
print type(dict)

print dict.items()

for i, j in dict.items():
    print i, '---->', j

for t in dict.items():
    print t
