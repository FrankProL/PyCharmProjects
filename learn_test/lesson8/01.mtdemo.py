#!/usr/bin/python
# encoding: utf-8


"""
@author: 大圣
@contact: excelchart@sina.cn
@file: 01.mtdemo.py
@time: 2015/12/18 0018 下午 10:35
"""

import threading
import time
class A(threading.Thread):
    def __init__(self,n):
        threading.Thread.__init__(self)
        self._n = n

    def run(self):
        while True:
            print 'in thread %s' % self._n
            time.sleep(1)

if __name__=='__main__':
    mt = [A(i) for i in range(4)]
    for t in mt:
        t.start()

    for t in mt :
        t.join()
