#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/14 14:52
# @Author  : Frank
# @Site    : 
# @File    : touchFile.py
# @Software: PyCharm
"""
import os
from datetime import timedelta, datetime

# hdfs dfs -rm /user/kzcq/input/kzmg/logs/kzmg_hunter_login/*

# '''按日期创建文件'''
# for i in range(180):
#     loginDate = datetime.today() + timedelta(-i)
#     dateStr = loginDate.strftime('%Y-%m-%d')
#     command='hdfs dfs -touchz /user/kzcq/input/kzmg/logs/kzmg_hunter_login/%s.txt'%(dateStr)
#     print (command)
#     os.system(command)

'''每晚定时执行，创建第二天的日志文件'''
loginDate = datetime.today() + timedelta(+3)
dateStr = loginDate.strftime('%Y-%m-%d')
command='hdfs dfs -touchz /user/kzcq/input/kzmg/logs/kzmg_hunter_login/%s.txt'%(dateStr)
print (command,datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
os.system(command)