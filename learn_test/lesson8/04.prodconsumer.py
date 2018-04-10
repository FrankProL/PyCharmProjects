#!/usr/bin/python
# encoding: utf-8


"""
@author: 大圣
@contact: excelchart@sina.cn
@file: 04.prodconsumer.py
@time: 2015/12/19 0019 上午 9:04
"""

import multiprocessing
import time
class Producer(multiprocessing.Process):
    def __init__(self,q):
        multiprocessing.Process.__init__(self)
        self._q = q

    def run(self):
        while True:
            self._q.put('time is %s' % time.time())
            time.sleep(1)


class Consumer(multiprocessing.Process):
    def __init__(self,q,n):
        multiprocessing.Process.__init__(self)
        self._q = q
        self._n = n

    def run(self):
        while True:
            msg =None
            try :
                msg = self._q.get()
            except :
                time.sleep(1)
                continue
            if msg:
                print 'in consumer %s %s' % (self._n,msg)


if __name__=='__main__':
    q = multiprocessing.Queue()
    producer = Producer(q)
    c1 = Consumer(q,1)
    c2 = Consumer(q,2)
    producer.start()
    c1.start()
    c2.start()
