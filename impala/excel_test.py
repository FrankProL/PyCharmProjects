#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/2/23 14:36
# @Author  : Frank
# @Site    : 
# @File    : excel_test.py
# @Software: PyCharm
"""
# import numpy as np
# import pandas as pd
#
# # prepare for data
# data = np.arange(1,34).reshape((11,3))
# data_df = pd.DataFrame(data)
#
# # change the index and column name
# data_df.columns = [u'2月9日',u'2月9日（123269）',u'2月9日（124770）']
# data_df.index = [u'历史首次充值人数',u'历史首次充值用户充值金额(当天充值)',u'竞猜题目数',u'房间登录用户数',u'房间登录用户充值人数',u'房间登录用户充值金额（去除红星闪闪）',
#                  u'房间登录用户首次充值人数',u'房间登录用户首次充值金额',u'房间登录用户数新增注册人数',u'房间登录用户数新增注册充值人数',u'房间登录用户数新增注册充值金额']
#
# # create and writer pd.DataFrame to excel
# writer = pd.ExcelWriter('Save_Excel.xlsx')
# data_df.to_excel(writer,u'充值注册',float_format='%.5f') # float_format 控制精度
# writer.save()

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
