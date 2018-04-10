#!/usr/bin/python
# encoding: utf-8


"""
@author: 大圣
@contact: excelchart@sina.cn
@file: 02.mysqldbdemo.py
@time: 2015/12/12 0012 下午 8:22
"""

import MySQLdb

conn = MySQLdb.connect(host='140.143.233.249',port=3306,user='root',
                       passwd='!Frank123456',db='test',charset='utf8')
conn.autocommit(True)
cursor = conn.cursor()

sqltext = ' select * from users'
cursor.execute(sqltext)
for row in cursor.fetchmany(2):
    print row

from faker import Factory
userfaker = Factory.create()

userinfo = [(userfaker.name(),userfaker.address(),userfaker.email()) for i in range(10)]

sql_template = 'insert into users (name,address,email) values (%s , %s ,%s)'
cursor.executemany(sql_template,userinfo)
cursor.close()
conn.close()