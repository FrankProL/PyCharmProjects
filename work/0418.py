#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/4/18 9:23
# @Author  : Frank
# @Site    : 
# @File    : 0418.py
# @Software: PyCharm
"""
import MySQLdb
import pandas as pd
import numpy as np
from impala.dbapi import connect

from datetime import timedelta, datetime
conn = connect(host='lg-15-163.ko.cn', port=21050)
cur = conn.cursor()

into_db = ("rr-bp1mku8v6xlq45tpco.mysql.rds.aliyuncs.com", "loujianfeng", "FeTuH9bo6fakUw9", "utf8", "live_core")
cnxn = MySQLdb.connect(host=into_db[0], user=into_db[1], passwd=into_db[2], charset=into_db[3], db=into_db[4])

data = pd.read_csv('tmp_data.csv', header=None)
data.columns = ['uid']
days=['06','07','08','09','10','11','12','13','14','15']
for i in range(6, 16):
    day = days[i - 6]
    # print ('----------------------%s 号--房间访问用户中是直播间新增用户的用户数------------------------' % i)
    sql = """select distinct user_id
    from stats_user_firstroom_v1
    where room_id=123557
    and create_time_day='2018-04-%s'
    """ % (day)
    cur.execute(sql)
    result = cur.fetchall()
    dd=pd.DataFrame(result)
    dd.columns=['user_id']
    user_id=list(dd['user_id'])
    userlist = ','.join(map(str, user_id))
    # print userlist



    sql = """select create_time,count(distinct user_id),count(user_id),sum(contribution)
from user_contribution
where create_time='2018-04-%s'
and room_id=123557
and behavior='behavior_send_gift'
and user_id in (%s)
group by create_time
order by create_time""" % (day,userlist)

    cursor = cnxn.cursor()

    cursor.execute(sql)
    result = cursor.fetchall()
    print result
    # df=pd.DataFrame(result)
    # print df

cursor.close()
cnxn.close()

cur.close()
conn.close()