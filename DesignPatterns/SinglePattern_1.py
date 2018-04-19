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

class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            orig=super(Singleton,cls)
            cls._instance=orig.__new__(cls,*args,**kw)
        return cls._instance