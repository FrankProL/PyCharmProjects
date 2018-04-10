#!/usr/bin/python
# encoding: utf-8


"""
@author: 大圣
@contact: excelchart@sina.cn
@file: 03.mpdemo.py
@time: 2015/12/19 0019 上午 9:00
"""


import multiprocessing
import time
class A(multiprocessing.Process):

    def __init__(self,n):
        multiprocessing.Process.__init__(self)
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
