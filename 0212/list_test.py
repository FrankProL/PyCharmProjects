#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/16 20:28
# @Author  : Frank
# @Site    : 
# @File    : list_test.py
# @Software: PyCharm
import time

l = [1, 2, 3, 'hello', 'hao are you']

print l
l = []
l.append(2)
print l
s = [8, 3, 9, 'hi']
l.extend(s)

print l

print l[2]

# 切片
print l[0:2]
print l[0:4:2]

print len(l)

print l * 4
print l + s
print 'hi' in l
print 4 in l

print cmp(l, s)
print max(l)
print min(l)

print l.count(3)
print l
# sort() 对原列表进行排序，返回结果None，原列表已排序
print l.sort()
print l

print l.index(3)

l.insert(0, 'one')
print l

# 移除列表中的一个元素，默认最后一个，并返回该元素的值
print l.pop()
print l
print l.pop(2)
# 排序、反转都是对列表自身操作
print l.reverse()
print l

print l.remove('one')
print l

x = range(1, 10, 1)
y = range(2, 11, 1)
# x+2
y * 2
x + y
print x
print y
print x + y
print y * 2

print x[::-1]  # -1 倒序排列
print x[2:4:1]

result = []
for i in x:
    if i < 4:
        result.append(i ** 2)
    else:
        result.append(i)
print result

# 列表解析
result2 = [i ** 2 for i in x if i < 4]
print result2

result3 = [i ** 2 if i < 4 else i for i in x]
print result3


def a(x):
    if x > 4:
        return True
    else:
        return False


print filter(a, x)


def b(x):
    if x < 4:
        return x ** 2
    else:
        return x


print map(b, x)

# 生成器表达式    generator
"""生成器是迭代的生成结果，而不是立刻对表达式求值
   得到的是个生成器对象，而不是列表
   不能用索引、append等列表操作
   可以用list()工厂函数转换为列表对象
"""
f=open('E:\Python\PythonExercise\\0202\u.data')

start1= time.clock()
lines=[t.split(',') for t in f]
end1=time.clock()
print type(lines)

print end1-start1

start2=time.clock()
lines2=(t.split(',') for t in f)
end2=time.clock()
print type(lines2)

print end2-start2