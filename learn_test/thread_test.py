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
        thread提供了低级别的、原始的线程以及一个简单的锁:
            thread.allocate_lock()  返回一个新的锁定对象。
            acquire() /release() 一个原始的锁有两种状态，锁定与解锁，分别对应acquire()和release() 方法。
"""
import thread
import time

locks=[]

def print_time(threadName,delay,lock):
    count=0
    while count<5:
        time.sleep(delay)
        count+=1
        print ('%s:%s'%(threadName,time.ctime(time.time())))
    lock.release()
    # # 可以等待线程被PVM回收，或主动调用exit或exit_thread方法结束线程
    # thread.exit_thread()

try:
    lock = thread.allocate_lock()
    lock.acquire()
    locks.append(lock)
    thread.start_new_thread(print_time,('thread-1',2,lock))
    lock = thread.allocate_lock()
    lock.acquire()
    locks.append(lock)
    thread.start_new_thread(print_time,('thread-2',4,lock))

except:
    print ('error: unable to start thread')

for i in locks:
    while i.locked():
        pass
# while 1:
#     pass