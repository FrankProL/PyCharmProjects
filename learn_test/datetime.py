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
import time

yesterday = datetime.today() + timedelta(-1)
print yesterday
yesterday_format = yesterday.strftime('%Y_%m_%d')
print yesterday_format
adate = yesterday.strftime('%Y-%m-%d')
bdate = yesterday.strftime('%Y%m%d')
print adate,bdate


"""更改日期"""
ddate = datetime(2018, 04, 27)
print (ddate)
print (type(ddate))
print (type(ddate.strftime("%Y-%m-%d %H:%M:%S")))

t= '2018-05-18'
timeArray =time.strptime(t,'%Y-%m-%d')
print (timeArray)
print(type(timeArray))
timeStamp=int(time.mktime(timeArray))
print (timeStamp)
print (time.time())

# print ddate.strptime()


# timeArray = time.strptime(ddate, "%Y-%m-%d %H:%M:%S")
# print (time.mktime(timeArray))

# python 3 用法
# today = datetime.date.today()
# print today
# yesterday = today - datetime.timedelta(days=1)
# print yesterday
# tomorrow = today + datetime.timedelta(days=1)
# print tomorrow