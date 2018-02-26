#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/2/18 15:21
# @Author  : Frank
# @Site    : 
# @File    : func_test.py
# @Software: PyCharm
"""
import time

'''python 函数可以有多个返回值，python默认自动封装成一个元组返回，如果有相应数量的变量接收，则python自动解封
   如果只有一个变量接收返回值，则不解封，直接返回一个元组
   为了提高程序可读性，通常手动封装成一个元组返回
'''


def fun1():
    a = 1
    b = 2
    c = 'hello'
    return a, b, c


x, y, z = fun1()
print x, type(x)
print y, type(y)
print z, type(z)

r = fun1()
print r, type(r)

# s, t = fun1()
# print r
# print t

"""函数也是对象，可以做参数传递、返回"""

def handleText(x):
    print 'text'
    print x

def handleHtml(x):
    print 'html'
    print x

def msg(x):
    if x == 'html':
        return handleHtml
    else:
        return handleText

msg('html')('helloword')

"""函数参数没有类型，python不做类型检查，
   不支持重载，python不会区分参数名字和个数
   多个函数重名时，后一个会覆盖前一个
   位置参数、关键词参数
"""
"""任意数量的参数：*，**
   定义函数时，是收集参数
        * ：用元组收集不匹配的位置参数
        **：用字典收集不匹配的关键字参数
        def fun(*args,**kwargs)
   调用函数时，是对参数解包
        * ：把一个集合打散成多个参数
        **：把一个字典打散成多个关键字参数
        fun(*args,**kwargs)
"""
def funA(x,y,z,*args,**kwargs):
    print x,y,z
    print args
    print kwargs
funA(1,2,3,4,5,6,7,a=12,b=23)

def funB(x,y,z):
    print x,y,z
x=[1,2,3]
y={'x':1,'y':'hello','z':'23'}
funB(x[0],x[1],x[2])    # 列表中的元素作为参数的两种方式
funB(*x)                # 列表中的元素作为参数的两种方式
funB(**y)               # 字典中的元素作为参数

"""引用传递、值传递"""
def funT(x):
    x=x+1
    print x
x=1
funT(x)
print x

def funS(x):
    x[1]='gengxin'
x=[1,2,3]
funS(x)
print x
"""函数作用域，LEGB
   local
   enclose任意上层的嵌套函数
   global全局（模块内）
   build-in 内置作用域
"""

"""函数文档属性 定义函数的第一个没有赋值的字符串，可以通过__doc__访问"""
a=10
def fundoc():
    '''
    @author
    :param
    :arg
    :return:
    '''
    global a
    a += 2
    print 'in function', a
fundoc()
print fundoc.__doc__

print help(fundoc)

"""函数式编程，函数也是对象，可以给函数增加属性"""
"""python函数可以嵌套定义，
   闭包，能够保留函数定义时的环境信息
        内部函数用到了外部函数中的变量
        外部函数返回内部函数
        def outer():
            def inner():
                ...
            return inner
"""
def f(x):
    y=222
    def inner(z):
        return x* y+z
    return inner
a10=f(14)
a20=f(20)
print a10,a20
print a10(14)
print a20(14)

"""装饰器
   不带参数装饰器
        # decorator(f)(*args,**kwargs)
        @decorator
        def f(): pass
    带参数装饰器
        # decorator(name)(f)(*args,**kwargs)
        @decorator(name)
        def f(): pass
"""
# 定义一个装饰器，就是一个嵌套函数，参数是要装饰的函数
def log(func):
    def wrapper(*args,**kwargs):
        print '~'*40
        start =time.clock()
        res=func(*args,**kwargs)
        end =time.clock()
        print 'calling ',func.__name__,args,kwargs
        print 'start at ',start,'end at ',end
        return  res
    return wrapper

def authorize(func):
    def wrapper(*args,**kwargs):
        if True:
            print 'welcome'
            return func(*args,**kwargs)
        else:
            print 'you are not allowed'
    return wrapper
# 定义一个带参数的装饰器，实质上就是多嵌套了一层，传递了一个参数进去
def logEx(name):
    def wrapper(func):
        def wrapper1(*args,**kwargs):
            print '~'*40
            start =time.clock()
            res=func(*args,**kwargs)
            end =time.clock()
            print name,'calling ',func.__name__,args,kwargs
            print 'start at ',start,'end at ',end
            return res
        return wrapper1
    return wrapper

@authorize
@logEx('frank')
def f1(x,y):
    return x+y
print f1(10,20)

# def f2(x,y):
#     print 'calling f2',x,y
#     start = time.clock()
#     z = x+y
#     end = time.clock()
#     print 'start at :',start,'end at ',end
#     return z
# f2(10,20)

"""迭代器
   permutations 排列
   combinations 组合
   product 笛卡尔积
   repeat 重复
   chain 链接一组迭代器
"""
import itertools
x = range(1,10)
citer= itertools.combinations(x,3)
for i in citer:
    print i

piter=itertools.permutations(x,2)
for i in piter:
    print i

z=['a','b','c','d']
y=range(1,4)
priter=itertools.product(z,y)
for i in priter:
    print i

c=itertools.chain(citer,piter,priter)
for i in c:
    print i

"""生成器
   生成器就是能够生成迭代器的东西
   生成器表达式得到的是生成器，而不是列表
   生成器函数
   yield
"""
def inc(n=1):
    while True:
        yield n     # 每次调用到此，返回n，并保存堆栈，下次调用继续向下执行
        n+=1

a=inc()
print type(a),a
print a.next(),a.next(),a.next()

# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
for cnt,x in enumerate(a):
    if cnt == 10:
        break
    else:
        print x

# 从文件夹中查找关键词
import os
def getFileList(rootDir):
    for path,dirlist,filelist in os.walk(rootDir):
        for filename in filelist:
            if filename.endswith('.csv'):
                yield os.path.join(path,filename)

def openFiles(filelist):
    for filename in filelist:
        yield (filename,open(filename))

def grep(filelist,pattern):
    for(filename,fh) in filelist:
        for line in fh:
            if pattern in line:
                yield (filename,line)

filelist=getFileList('E:\Python\\aPython')
files=openFiles(filelist)
lines= grep(files,'6.000')

for (filename,line) in lines:
    print '~'*60
    print filename
    print line
