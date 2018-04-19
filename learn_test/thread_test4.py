#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/4/19 15:00
# @Author  : Frank
# @Site    : 
# @File    : thread_test4.py
# @Software: PyCharm
"""
"""线程优先级队列"""
import threading
import time
import Queue

exitFlag=0

class myThread(threading.Thread):
    def __init__(self,threadID,name,q):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.q=q
    def run(self):
        print('starting:'+self.name)
        process_data(self.name,self.q)
        print('exiting:'+self.name)

def process_data(threadName,q):
    while not exitFlag:
        queneLock.acquire()
        if not workQueue.empty():
            data=q.get()
            queneLock.release()
            print ('%s processing %s ' % (threadName,data))
        else:
            queneLock.release()
        time.sleep(1)


threadList= ['thread-1','thread-2','thread-3']
nameList= ['one','two','three','four','five']
queneLock=threading.Lock()
workQueue=Queue.Queue(10)

threads=[]
threadID=1

# 创建新线程
for tName in threadList:
    thread=myThread(threadID,tName,workQueue)
    thread.start()
    threads.append(thread)
    threadID+=1

# 填充队列
queneLock.acquire()
for word in nameList:
    workQueue.put(word)
queneLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag=1

# 等待所有线程完成
for t in threads:
    t.join()
print ('eixting main thread')