#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/4/27 14:16
# @Author  : Frank
# @Site    : 
# @File    : 0427_recharge.py
# @Software: PyCharm
"""
import MySQLdb
from impala.dbapi import connect
import pandas as pd

conn = connect(host='lg-15-163.ko.cn', port=21050)
cur = conn.cursor()

sql="""select create_time_month,user_id,sum(recharge_gold)/1000 as gold
from stats_user_recharge_v1
where recharge_gold>0
and create_time_month>='2018-01'
group by create_time_month,user_id"""

cur.execute(sql)
result=cur.fetchall()
df=pd.DataFrame(result,columns=['create_time','user_id','recharge'])
# print(df)
user_id = list(df['user_id'])

userlist = ','.join(map(str, user_id))

into_db = ("rr-bp1mku8v6xlq45tpco.mysql.rds.aliyuncs.com", "loujianfeng", "FeTuH9bo6fakUw9", "utf8", "live_core")
cnxn = MySQLdb.connect(host=into_db[0], user=into_db[1], passwd=into_db[2], charset=into_db[3], db=into_db[4])
cursor = cnxn.cursor()

sql="""select id,nickname
from user
where id in (%s)"""%userlist

cursor.execute(sql)
result=cursor.fetchall()
dfsql=pd.DataFrame(list(result),columns=['user_id','nickname'])

new=pd.merge(df,dfsql,on='user_id',how='left')
new[['create_time','user_id','nickname','recharge']].to_excel('recharge2.xlsx', u'recharge', float_format='%.5f',index=False)


cursor.close()
cnxn.close()
cur.close()
conn.close()