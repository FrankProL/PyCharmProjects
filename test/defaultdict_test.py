#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/3/14 10:56
# @Author  : Frank
# @Site    : 
# @File    : defaultdict_test.py
# @Software: PyCharm
"""
from collections import defaultdict
"""Using list as the default_factory, it is easy to group a sequence of key-value pairs into a dictionary of lists:"""
# https://segmentfault.com/a/1190000010081065
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k,v in s:
    print k,'--',v
    d[k].append(v)
print (d.items())
print (type(d))

print ("""===========================""")
dd={}
for k,v in s:
    if dd.has_key(k):
        dd[k].append(v)
    else:
        dd[k]=[]
        dd[k].append(v)
print (dd)

print ("""===========================""")
dd={}
for k,v in s:
    dd.setdefault(k,[])
    dd[k].append(v)
print (dd)