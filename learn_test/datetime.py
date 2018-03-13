#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/2/24 11:05
# @Author  : Frank
# @Site    : 
# @File    : datetime.py
# @Software: PyCharm
"""
from datetime import timedelta, datetime

yesterday = datetime.today() + timedelta(-1)
print yesterday
yesterday_format = yesterday.strftime('%Y_%m_%d')
print yesterday_format
adate = yesterday.strftime('%Y-%m-%d')
bdate = yesterday.strftime('%Y%m%d')
print adate,bdate

# python 3 用法
# today = datetime.date.today()
# print today
# yesterday = today - datetime.timedelta(days=1)
# print yesterday
# tomorrow = today + datetime.timedelta(days=1)
# print tomorrow