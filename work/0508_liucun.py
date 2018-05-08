#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/4/17 15:34
# @Author  : Frank
# @Site    : 
# @File    : 0417.py
# @Software: PyCharm
"""
import MySQLdb
import pandas as pd
import numpy as np
from impala.dbapi import connect

from datetime import timedelta, datetime

yesterday = datetime.today() + timedelta(-1)
print (yesterday)
adate = yesterday.strftime('%Y-%m-%d')
bdate = yesterday.strftime('%Y%m%d')
print (adate, bdate)

list_adate = []
list_bdate = []
list_cdate = []
ddate = datetime(2018, 04, 20)
for i in range(10):
    tmp = ddate + timedelta(+i)
    adate = tmp.strftime('%Y-%m-%d')
    list_adate.append(adate)

ddate = datetime(2018, 04, 21)
for i in range(17):
    tmp = ddate + timedelta(+i)
    bdate = tmp.strftime('%Y%m%d')
    cdate = tmp.strftime('%Y-%m-%d')
    list_bdate.append(bdate)
    list_cdate.append(cdate)

conn = connect(host='lg-15-163.ko.cn', port=21050)
cur = conn.cursor()

into_db = ("rr-bp1mku8v6xlq45tpco.mysql.rds.aliyuncs.com", "loujianfeng", "FeTuH9bo6fakUw9", "utf8", "live_core")
cnxn = MySQLdb.connect(host=into_db[0], user=into_db[1], passwd=into_db[2], charset=into_db[3], db=into_db[4])

days = list_adate
# day_t = list_bdate
day_t = list_cdate
for i in range(10):
    day = days[i]

    print ('----------------------%s 号--房间访问用户中是直播间新增用户的用户数------------------------' % day)

    sql = """select user_id
    from stats_user_firstroom_v1
    where room_id=124961
    and create_time_day='%s'
    """ % (day)
    cur.execute(sql)
    result = cur.fetchall()
    if result:
        dd = pd.DataFrame(result)
        dd.columns = ['user_id']
        user_id = list(dd['user_id'])
        userlist = ','.join(map(str, user_id))
        # print userlist

    for j in range(7):
        dtime = day_t[i + j]
        # sql="""select day,count(distinct uid)
        # from ssets_weblogs201
        # where roomid='124961'
        # and day='%s'
        # and uid>'0'
        # and cast(uid as int) in (select user_id
        # from stats_user_firstroom_v1
        # where room_id=124961
        # and create_time_day='%s'
        # )
        # group by day"""%(dtime,day)
        # cur.execute(sql)
        # result=cur.fetchall()
        # print result

        sql="""select create_time,count(distinct user_id)
        from user_contribution
        where create_time='%s'
        and room_id=124961
        and behavior='behavior_send_gift'
        and user_id in (%s)
        group by create_time
        order by create_time"""%(dtime,userlist)
        cursor = cnxn.cursor()

        cursor.execute(sql)
        result = cursor.fetchall()
        print result

cursor.close()
cnxn.close()
cur.close()
conn.close()
