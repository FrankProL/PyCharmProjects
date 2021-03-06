#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/4/19 16:30
# @Author  : Frank
# @Site    : 
# @File    : SinglePattern_1.py
# @Software: PyCharm
"""
import threading
import time

# 这里使用__new__来实现单例模式
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance

# 总线
class Bus(Singleton):
    lock = threading.RLock()

    def sendData(self, data):
        self.lock.acquire()
        time.sleep(3)
        print('Sending Signal Data...' + data)
        self.lock.release()

# 线程对象，为更加说明单例的含义，这里讲bus对象实例化写在了run里
class VisitEntity(threading.Thread):
    my_bus = ''
    name = ''

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def run(self):
        self.my_bus = Bus()
        self.my_bus.sendData(self.name)


if __name__ == '__main__':
    for i in range(3):
        print('Entity %d begin to run...' % i)
        my_entity = VisitEntity()
        my_entity.setName('Entity_' + str(i))
        my_entity.start()
