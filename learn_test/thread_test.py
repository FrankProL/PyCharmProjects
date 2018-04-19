#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/4/16 18:39
# @Author  : Frank
# @Site    : 
# @File    : thread_test.py
# @Software: PyCharm
"""
"""Python中使用线程有两种方式：函数或者用类来包装线程对象
        函数式：调用thread模块中的start_new_thread()函数来产生新线程。语法如下:
            thread.start_new_thread ( function, args[, kwargs] )
"""
import thread
import time

def print_time(threadName,delay):
    count=0
    while count<5:
        time.sleep(delay)
        count+=1
        print ('%s:%s'%(threadName,time.ctime(time.time())))

try:
    thread.start_new_thread(print_time,('thread-1',2,))
    thread.start_new_thread(print_time,('thread-2',4,))
except:
    print ('error: unable to start thread')

while 1:
    pass