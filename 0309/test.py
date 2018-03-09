#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/3/9 14:47
# @Author  : Frank
# @Site    : 
# @File    : test.py
# @Software: PyCharm
"""
import ConfigParser
import platform

print platform.system()
config=ConfigParser.ConfigParser()
config.read('info.prop')

if platform.system()=='Windows':
    path=config.get('plat', 'windows')
    print path
else:
    path=config.get('plat', 'linux')
    print path
with open(path) as file:
    for line in file:
        print line
