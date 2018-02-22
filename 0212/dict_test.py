#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/2/19 11:35
# @Author  : Frank
# @Site    : 
# @File    : dict_test.py
# @Software: PyCharm
"""
x={'name':'zhangsan','home':'beijing'}
y=dict(name='lisi',home='zhengzhou')    # 通过字典的工厂函数创建
print x,y

for i in x :
    print i # 获取的是key
    print x[i] # 获取的是value

for i in x.items():
    print i,type(i)     # 获取的是key、value元组

for key,value in x.items():
    print key
    print value

# print x['name1']        # 获取对应key的value值，不存在的话会有KeyError异常
print x.get('name1')    # 不存在对应key的话，返回None
print x.get('name1', 'not exists')

x['a']=10
print x
x['a']=11
print x
print x.setdefault('a',13)      # 向字典中添加值，如果key中已有，则返回对应的value，value值不变
print x
print x.setdefault('b',100)     # 如果key中对应的key，则添加key、value
print x

x.update(y)     # 将字典y的值添加到x中，如果x，y中有key重复，用y的值更新x的值
print x

"""可变对象，不可变对象"""
a='wangwu'
b=range(1,10)
print hash(a)
# print hash(b)

