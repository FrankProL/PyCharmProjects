#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/4/19 11:29
# @Author  : Frank
# @Site    : 
# @File    : thread_test2.py
# @Software: PyCharm
"""
""" Python通过两个标准库thread和threading提供对线程的支持。thread提供了低级别的、原始的线程以及一个简单的锁。threading 模块提供的其他方法
    使用Threading模块创建线程，直接从threading.Thread继承，然后重写__init__方法和run方法：
"""
import threading
import time

exitFlag = 0


class myThread(threading.Thread):               # 继承父类thread.Thread
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay

    def run(self):                              # 要执行的代码写到run函数里面，线程在创建后会直接运行run函数
        print ('starting: ' + self.name)
        print_time(self.name, self.delay, 5)
        print ('existing: ' + self.name)


def print_time(threadName, delay, counter):
    while (counter):
        if exitFlag:
            (threading.Thread).exit()
        time.sleep(delay)
        print ('%s:%s' % (threadName, time.ctime(time.time())))
        counter -= 1


# 创建新线程
thread1 = myThread(1, 'thread-1', 1)
thread2 = myThread(2, 'thread-2', 2)
# 开启线程
thread1.start()
thread2.start()

print ('exiting main thread')
