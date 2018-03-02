#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/2/26 14:25
# @Author  : Frank
# @Site    : 
# @File    : Excel_test.py
# @Software: PyCharm
"""
import numpy as np
import pandas as pd

from datetime import timedelta, datetime

yesterday = datetime.today() + timedelta(-1)
title_1= yesterday.strftime('%m月%d日')
title_2= yesterday.strftime('%m月%d日(123269)')
title_3= yesterday.strftime('%m月%d日(124770)')

# prepare for data
data = np.arange(1, 34).reshape((11, 3))
data_df = pd.DataFrame(data)

# change the index and column name
data_df.columns = ['%s' % (title_1),'%s' % (title_2),'%s' % (title_3)]
data_df.index = [u'历史首次充值人数', u'历史首次充值用户充值金额(当天充值)', u'竞猜题目数', u'房间登录用户数', u'房间登录用户充值人数', u'房间登录用户充值金额（去除红星闪闪）',
                 u'房间登录用户首次充值人数', u'房间登录用户首次充值金额', u'房间登录用户数新增注册人数', u'房间登录用户数新增注册充值人数', u'房间登录用户数新增注册充值金额']

# create and writer pd.DataFrame to excel
writer = pd.ExcelWriter('Save_Excel.xlsx')
data_df.to_excel(writer, u'充值注册', float_format='%.5f')  # float_format 控制精度
writer.save()

"""使用pandas读取excel文件"""
xls_file = pd.ExcelFile('Save_Excel.xlsx')
xls_file.sheet_names  # 显示出读入excel文件中的表名字
table1 = xls_file.parse(u'充值注册')
# table2=xls_file.parse('second_sheet')
print table1
print type(table1)
# xlsx_file=pd.ExcelFile("./demo.xlsx")
# x1=xlsx_file.parse(0)
# x2=xlsx_file.parse(1)

# excel文件的写出,只有DataFrame对象才能使用to_excel方法。
# pd.DataFrame(data).to_excel("abc.xlsx",sheet_name="123",index=False,header=True)
# excel文件和pandas的交互读写，主要使用到pandas中的两个函数,一个是pd.ExcelFile函数,一个是to_excel函数

"""另一种读取方式"""
pos = pd.read_excel('Save_Excel.xlsx')
print pos
pos = pd.read_excel('Save_Excel.xlsx', header=None)
print pos


"""使用openpyxl和pandas"""
from openpyxl import load_workbook
data = pd.read_excel('Save_Excel.xlsx', sheetname=u'充值注册')
# col_data = list(data.ix[:, 3])  # 获取除表头外开始的第三列数据
row_data = list(data.ix[5,:])  # 获取除表头外开始的第五行数据

writer = pd.ExcelWriter( 'Save_Excel.xlsx', engine='openpyxl')
book = load_workbook('Save_Excel.xlsx')
writer.book = book
result = pd.DataFrame(row_data)
result.to_excel(writer,sheet_name='a', index=False)
writer.save()
