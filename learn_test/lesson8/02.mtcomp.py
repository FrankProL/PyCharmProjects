#!/usr/bin/python
# encoding: utf-8


"""
@author: 大圣
@contact: excelchart@sina.cn
@file: 02.mtcomp.py
@time: 2015/12/18 0018 下午 10:43
"""

from faker import Factory
faker=Factory.create()
cnt = 100000
x1=[faker.paragraph() for i in range(cnt)]
x2=[faker.paragraph() for i in range(cnt)]

import time
#1、单线程
start = time.clock()
for one in x1:
    len(one)
for one in x2:
    len(one)
end = time.clock()

print 'single thread is %s' % (end-start)

import threading
class A(threading.Thread):
    def __init__(self,x):
        threading.Thread.__init__(self)
        self.x=x
    def run(self):
        for each in self.x:
            len(each)

t1=A(x1)
t2=A(x2)
start1 = time.clock()
t1.start()
t2.start()
t1.join()
t2.join()
end1=time.clock()

print 'two thread is %s' % (end1-start1)

print (end1-start1)/(end-start)