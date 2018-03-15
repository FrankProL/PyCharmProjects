#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/3/13 14:44
# @Author  : Frank
# @Site    : 
# @File    : onelinepy.py
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

"""输出心形字符图案"""
print('\n'.join([''.join([('PYTHON!'[(x-y)%7] if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else ' ') for x in range(-30,30)]) for y in range(15,-15,-1)]))

"""一行代码输出Mandelbrot图象
   Mandelbrot图象：图象中的每个位置都对应公式N=x+y*i中的一个复数
"""
print'\n'.join([''.join(['*'if abs((lambda a:lambda z,c,n:a(a,z,c,n))(lambda s,z,c,n:z if n==0else s(s,z*z+c,c,n-1))(0,0.02*x+0.05j*y,40))<2 else' 'for x in range(-80,20)])for y in range(-20,20)])

"""八皇后问题"""
_=[__import__('sys').stdout.write("\n".join('.' * i + 'Q' + '.' * (8-i-1) for i in vec) + "\n===\n") for vec in __import__('itertools').permutations(xrange(8)) if 8 == len(set(vec[i]+i for i in xrange(8))) == len(set(vec[i]-i for i in xrange(8)))]

"""一行代码解决FizzBuzz问题
   FizzBuzz问题：打印数字1到100,3的倍数打印Fizz，5的倍数打印Buzz，即使3又是5的倍数打印FizzBuzz
"""
for x in range(1, 101): print("fizz"[x % 3 * 4:]+"buzz"[x % 5 * 4:] or x)

"""一行代码启动一个web服务
        python -m SimpleHTTPServer 8080  # python2
        python3 -m http.server 8080  # python3
   Python之禅，一行代码输出“The Zen of Python”
        python -c "import this"   或者直接python命令里、脚本里 import this
"""

"""一行代码实现变量值互换"""
a, b = 1, 2
a, b = b, a
print (a, b)

"""一行代码打印9x9乘法表"""
print('\n'.join([' '.join(['%s*%s=%-2s' % (y, x, x*y) for y in range(1, x+1)]) for x in range(1, 10)]))

"""一行代码输出1-100之间的素数"""
print(' '.join([str(item) for item in filter(lambda x: not [x % i for i in range(2, x) if x % i == 0], range(2, 101))]))
print(' '.join([str(item) for item in filter(lambda x: all(map(lambda p: x % p != 0, range(2, x))), range(2, 101))]))

"""一行代码输出斐波那契数列"""
print([x[0] for x in [(a[i][0], a.append([a[i][1], a[i][0]+a[i][1]])) for a in ([[1, 1]],) for i in range(30)]])

"""一行实现快排算法"""
qsort = lambda arr: len(arr) >= 1 and qsort(list(filter(lambda x: x <= arr[0], arr[1:]))) + arr[0:1] + qsort(list(filter(lambda x: x > arr[0], arr[1:]))) or arr
l = [1, 39, 20, 5, 3, 9, 8]
print l
print qsort(l)

"""一行代码实现数组的flatten功能，将多为数组转化为一维"""
flatten = lambda x: [y for l in x for y in flatten(l)] if isinstance(x, list) else [x]
l = [[1, 2, 3], [4, 7, 8]]
print flatten(l)

"""一行代码实现list分组
"""
a=[3, 8, 9, 4, 1, 10, 6, 7, 2, 5]
array = lambda x: [x[i:i+3] for i in range(0, len(x), 3)]
print array(a)

"""看不懂的表白"""
(lambda _, __, ___, ____, _____, ______, _______, ________: getattr(
    __import__(True.__class__.__name__[_] + [].__class__.__name__[__]),
    ().__class__.__eq__.__class__.__name__[:__] + ().__iter__().__class__.__name__[_____:________])(_, (
lambda _, __, ___: _(_, __, ___))(
    lambda _, __, ___: chr(___ % __) + _(_, __, ___ // __) if ___ else (lambda: _).func_code.co_lnotab, ____ << ______,
    (((_____ << _____) + _______) << ((_ << _______) + (_ << __))) - (
    ((((___ << __) + _) << ____) - _) << ((((_ << ____) - _) << ___) + _)) - (
    ((_____ << _____) + _______) << ((_______ << ____))) + (
    ((___ << _____) - ___) << ((((___ << __) + _) << ___) - _)) - (
    ((((___ << __) - _) << ____) + _____) << ((___ << _____) - ___)) + (
    ((_______ << ____) - ___) << ((_____ << ____) + ___)) + (
    ((((___ << __) - _) << ___) + _) << (((((_ << ___) + _)) << ___) + (_ << _))) + (
    ((((___ << __) + _) << ___) - ___) << ((_ << ______))) + (((_____ << ____) - ___) << ((_______ << ___))) + (
    ((_ << ______) + _) << ((___ << ____) - _)) - (((((___ << __) + _) << __) + _) << ((_____ << ___) - _)) - (
    ((_____ << __) - _) << ((_ << _____) - _)) - (((_ << _____) + _) << ((___ << ___) - _)) - (
    _____ << (((((_ << ___) + _)) << _))) + (_ << (((___ << __) + _))) + (((((_ << ___) + _))) << ___) + _)))(
    *(lambda _, __: _(_, __))(lambda _, __: [__[(lambda: _).func_code.co_nlocals].func_code.co_argcount] + _(_, __[(
    lambda _: _).func_code.co_nlocals:]) if __ else [], (
                              lambda _: _, lambda _, __: _, lambda _, __, ___: _, lambda _, __, ___, ____: _,
                              lambda _, __, ___, ____, _____: _, lambda _, __, ___, ____, _____, ______: _,
                              lambda _, __, ___, ____, _____, ______, _______: _,
                              lambda _, __, ___, ____, _____, ______, _______, ________: _)))
"""矩阵转置"""
m = [[1, 2], [3, 4]]
print zip(*m)

"""一行统计一本书的所有词频(此处是前100)：Counter(re.findall(r'\w+',open('hamlet.txt').read().lower())).most_common(100)记得：import re; from collections import Counter
"""
"""给一个表达式，求计算结果"""
print input()

"""求解2的1000次方的各位数之和"""
print(sum(map(int, str(2**1000))))