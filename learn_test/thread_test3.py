#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/4/19 14:25
# @Author  : Frank
# @Site    : 
# @File    : thread_test3.py
# @Software: PyCharm
"""
"""线程同步
    acquire方法和release方法，对于那些需要每次只允许一个线程操作的数据，可以将其操作放到acquire和release方法之间
"""
import threading
import time


class myThread(threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay

    def run(self):
        print ('starting : ' + self.name)
        threadLock.acquire()  # 获得锁，成功返回True，可选参数timeout不填，则一直阻塞直到获得锁定，否则超时将返回False
        print_time(self.name, self.delay, 3)
        threadLock.release()  # 释放锁


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print('%s:%s' % (threadName, time.ctime(time.time())))
        counter -= 1


threadLock = threading.Lock()
threads = []

# 创建线程
thread1 = myThread(1, 'thread-1', 1)
thread2 = myThread(2, 'thread-2', 2)

# 启动线程
thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

# 等待所有线程结束
for t in threads:
    t.join()
print ('exiting main thread')
