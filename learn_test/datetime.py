#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/2/24 11:05
# @Author  : Frank
# @Site    : 
# @File    : datetime.py
# @Software: PyCharm
https://blog.csdn.net/p9bl5bxp/article/details/54945920
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


"""更改日期 、   日期时间转为时间戳"""
ddate = datetime(2018, 04, 27)
print (ddate)
print (type(ddate))
print (type(ddate.strftime("%Y-%m-%d %H:%M:%S")))

t= '2018-05-18'
timeArray =time.strptime(t,'%Y-%m-%d')   # 转为时间数组
print (timeArray)
print(type(timeArray))
timeStamp=int(time.mktime(timeArray))
print (timeStamp)
print (time.time())

# print ddate.strptime()
# timeArray = time.strptime(ddate, "%Y-%m-%d %H:%M:%S")
# print (time.mktime(timeArray))

"""时间戳转换为指定格式的日期"""
# 使用time
timeStamp = 1381419600
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
print (otherStyleTime)   # 2013--10--10 23:40:00
# 使用datetime
timeStamp = 1381419600
dateArray =datetime.utcfromtimestamp(timeStamp)
otherStyleTime = dateArray.strftime("%Y--%m--%d %H:%M:%S")
print (otherStyleTime)   # 2013--10--10 15:40:00

"""更改str类型日期的显示格式"""
tss2 = "2013-10-10 23:40:00"
timeArray = time.strptime(tss2, "%Y-%m-%d %H:%M:%S")
# 转为其它格式
otherStyleTime = time.strftime("%Y/%m/%d %H:%M:%S", timeArray)
print (otherStyleTime)  # 2013/10/10 23:40:00

tss3 = "2013/10/10 23:40:00"
timeArray = time.strptime(tss3, "%Y/%m/%d %H:%M:%S")
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print (otherStyleTime)  # 2013-10-10 23:40:00

"""获取当前时间并且用指定格式显示"""
# 获取当前时间戳
now = int(time.time())
timeArray = time.localtime(now)
otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
print (otherStyleTime)    # 2017--12--11 19:18:02

# 获取当前时间，数组格式
now = datetime.now()
otherStyleTime = now.strftime("%Y--%m--%d %H:%M:%S")
print (otherStyleTime)   # 2017--12--11 19:18:02



# python 3 用法
# today = datetime.date.today()
# print today
# yesterday = today - datetime.timedelta(days=1)
# print yesterday
# tomorrow = today + datetime.timedelta(days=1)
# print tomorrow