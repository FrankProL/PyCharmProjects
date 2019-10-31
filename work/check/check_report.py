#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import pymysql
import logging

# 监控数据库信息
mysql_ip='192.168.1.11'
mysql_port='3306'
mysql_username='report'
mysql_pass='gC4GKVdAaZpdJUhp'
mysql_dbname='basicstat'




##线上报表数据库信息
report_mysql_ip='192.168.1.11'
report_mysql_port='3306'
report_mysql_username='report'
report_mysql_pass='gC4GKVdAaZpdJUhp'
report_mysql_dbname='basicstat'
report_sql="SELECT COUNT(1) FROM %s WHERE %s >= DATE_FORMAT(DATE_SUB(CURDATE(),INTERVAL %s),'%s')"
update_report_sql= "UPDATE bigdata_report_monitor_config set data_cnt=%s,last_check_time=now() where tbl_name = '%s' "

# 打开数据库连接
db = pymysql.connect(mysql_ip, mysql_username, mysql_pass, mysql_dbname)
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# SQL
sql = "SELECT tbl_name,col_name,delay_monitor_time,data_type FROM bigdata_report_monitor_config where tbl_name !='NULL' and monitor_type !='时' and is_monitor='Y'"
# 执行SQL语句
cursor.execute(sql)
result = cursor.fetchall()

f = open('/var/log/report_monitor.log', 'w')

for i in result:
	try:
		report_db = pymysql.connect(report_mysql_ip, report_mysql_username, report_mysql_pass, report_mysql_dbname)
		report_cursor = report_db.cursor()
		report_cursor.execute(report_sql %(i[0],i[1],i[2],i[3]))
		report_result = report_cursor.fetchone()
		report_db.close()
	except:
		f.write(str(i[0])+','+str(0)+'\n')
		cursor.execute(update_report_sql %(0,i[0]))
	else:
		f.write(str(i[0])+','+str(report_result[0])+'\n')
		cursor.execute(update_report_sql %(report_result[0],i[0]))

f.close()
db.commit()
db.close()

