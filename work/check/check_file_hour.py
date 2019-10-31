#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/10/8 11:15
# @Author  : Frank
# @Site    : 
# @File    : check_file_hour.py
# @Software: PyCharm
"""


import pymysql
import os

# 监控数据库信息
mysql_ip='192.168.1.11'
mysql_port='3306'
mysql_username='report'
mysql_pass='gC4GKVdAaZpdJUhp'
mysql_dbname='basicstat'


command="hadoop dfs -ls %s/`%s`/%s"
update_report_sql= "UPDATE bigdata_file_monitor_config set data_cnt=%s,last_check_time=now() where monitor_name = '%s' "

# 打开数据库连接
db = pymysql.connect(mysql_ip, mysql_username, mysql_pass, mysql_dbname,charset='utf8')
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# SQL
sql = "SELECT monitor_name,dir_path,file_path,data_type FROM bigdata_file_monitor_config where  monitor_type ='时' and is_monitor='Y' "
# 执行SQL语句
cursor.execute(sql)
result = cursor.fetchall()
f = open('/var/log/monitor_file_hour.log', 'w')

for i in result:
        result=os.system(command %(i[1],i[3],i[2]))
        f.write(i[0]+','+str(result)+'\n')
        cursor.execute(update_report_sql %(result,i[0]))

f.close()
db.commit()
db.close()