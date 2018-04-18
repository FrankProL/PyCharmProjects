#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/4/17 15:34
# @Author  : Frank
# @Site    : 
# @File    : 0417.py
# @Software: PyCharm
"""
import pandas as pd
import numpy as np
from impala.dbapi import connect

from datetime import timedelta, datetime

yesterday = datetime.today() + timedelta(-1)
print (yesterday)
adate = yesterday.strftime('%Y-%m-%d')
bdate = yesterday.strftime('%Y%m%d')
print (adate, bdate)

# conn = connect(host='lg-15-163.ko.cn', port=21050)
# cur = conn.cursor()
#
# sql = """select distinct uid
# from ssets_weblogs201
# where roomid='123557'
# and day='20180415'
# and uid>'0'"""
# cur.execute(sql)
# result = cur.fetchall()
# # print result
# df=pd.DataFrame(list(result))
# df.to_csv('tmp_data_15.csv',index=False,header=False)
# cur.close()
# conn.close()
data=pd.read_csv('tmp_data.csv',header=None)
data.columns=['uid']
data6=pd.read_csv('tmp_data_6.csv',header=None)
data6.columns=['uid6']
data7=pd.read_csv('tmp_data_7.csv',header=None)
data7.columns=['uid7']
data8=pd.read_csv('tmp_data_8.csv',header=None)
data8.columns=['uid8']
data9=pd.read_csv('tmp_data_9.csv',header=None)
data9.columns=['uid9']
data10=pd.read_csv('tmp_data_10.csv',header=None)
data10.columns=['uid10']
data11=pd.read_csv('tmp_data_11.csv',header=None)
data11.columns=['uid11']
data12=pd.read_csv('tmp_data_12.csv',header=None)
data12.columns=['uid12']
data13=pd.read_csv('tmp_data_13.csv',header=None)
data13.columns=['uid13']
data14=pd.read_csv('tmp_data_14.csv',header=None)
data14.columns=['uid14']
data15=pd.read_csv('tmp_data_15.csv',header=None)
data15.columns=['uid15']

dd=pd.merge(data6,data,left_on='uid6',right_on='uid',how='left')

print ('----------------------6------------------------')
print len(dd[pd.isnull(dd['uid'])]['uid6'])

print ('----------------------------------------------')
print len(data['uid'])
data6.columns=['uid']
data=data.append(data6)
data=data.drop_duplicates()
print len(data['uid'])
print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

dd=pd.merge(data7,data,left_on='uid7',right_on='uid',how='left')

print ('----------------------7------------------------')
print len(dd[pd.isnull(dd['uid'])]['uid7'])

print ('----------------------------------------------')
print len(data['uid'])
data7.columns=['uid']
data=data.append(data7)
data=data.drop_duplicates()
print len(data['uid'])
print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
dd=pd.merge(data8,data,left_on='uid8',right_on='uid',how='left')

print ('----------------------7------------------------')
print len(dd[pd.isnull(dd['uid'])]['uid8'])

print ('----------------------------------------------')
print len(data['uid'])
data8.columns=['uid']
data=data.append(data8)
data=data.drop_duplicates()
print len(data['uid'])
