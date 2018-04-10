#!/usr/bin/python
# encoding: utf-8


"""
@author: 大圣
@contact: excelchart@sina.cn
@file: 01.connectordemo.py
@time: 2015/12/12 0012 下午 7:38
"""
from mysql import connector
conn = connector.connect(host='localhost',port=3306,user='root',
                         password='root',database='test',charset='utf8')
conn.autocommit = True
cursor = conn.cursor()
# sqltext = 'insert into users(name,address,email) values ("dasheng","beijing","abc@def")'
# cursor.execute(sqltext)
# cursor.close()
# conn.close()

# sqltext = ' select * from users'
# cursor.execute(sqltext)
# for row in cursor:
#     print row
#
# cursor.close()
# conn.close()

from faker import Factory
userfaker = Factory.create()

userinfo = [(userfaker.name(),userfaker.address(),userfaker.email()) for i in range(10)]

sql_template = 'insert into users (name,address,email) values (%s , %s ,%s)'
cursor.executemany(sql_template,userinfo)
cursor.close()
conn.close()