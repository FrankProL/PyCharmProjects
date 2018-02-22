#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/2/19 14:34
# @Author  : Frank
# @Site    : 
# @File    : set_test.py
# @Software: PyCharm
"""
"""set集合只能通过set()工厂函数来创建，有set 和fronzenset """
x=set(range(3,18,2))
print x
y=set(range(1,10))
print y
z=frozenset(range(2,20,2))
print z
w=set([21,22])
print w
"""集合操作"""
print '并集：', x|y
print '交集：', x&y
print '差集：', x-y
print '对称差集：', x^y
# print '', x|=y
print 'x是否是y的子集：', x<y
print 'x是否是y的超集：', x>y
print 'x和y是否有交集：', x.isdisjoint(z)

# 可变集合
x.add(33)
print x
# x.remove(34)          # 移除元素，如果不存在报错
x.discard(34)           # 移除元素，如果不存在忽略
x.difference_update(y)  # 删除交集
print x
x.update(y)             # 用y更新x
print x
x.clear()
print x