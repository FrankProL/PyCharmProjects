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

conn = connect(host='lg-15-163.ko.cn', port=21050)
cur = conn.cursor()

into_db = ("rr-bp1mku8v6xlq45tpco.mysql.rds.aliyuncs.com", "loujianfeng", "FeTuH9bo6fakUw9", "utf8", "live_core")
cnxn = MySQLdb.connect(host=into_db[0], user=into_db[1], passwd=into_db[2], charset=into_db[3], db=into_db[4])

days=['13','14','15','16','17','18','19','20','21','22']
# days=['06','07','08','09','10','11','12','13','14','15']
day_t=['07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22']
for i in range(10):
    day=days[i]

    print ('----------------------%s 号--房间访问用户中是直播间新增用户的用户数------------------------'%day)

    sql = """select user_id
    from stats_user_firstroom_v1
    where room_id=123176
    and create_time_day='2018-04-%s'
    """ % (day)
    cur.execute(sql)
    result = cur.fetchall()
    if result:
        dd=pd.DataFrame(result)
        dd.columns=['user_id']
        user_id=list(dd['user_id'])
        userlist = ','.join(map(str, user_id))
        # print userlist

    #     sql="""select create_time,count(distinct user_id),count(user_id),sum(contribution)
    # from user_contribution
    # where create_time='2018-04-%s'
    # and room_id=123176
    # and behavior='behavior_send_gift'
    # and user_id in (%s)
    # group by create_time
    # order by create_time"""%(day,userlist)
    #     cursor = cnxn.cursor()
    #
    #     cursor.execute(sql)
    #     result = cursor.fetchall()
    #     print result


        sql = """select create_time_day,sum(recharge_gold) as gold ,count(distinct user_id) as num
    from stats_user_recharge_v1
    where recharge_gold>0
    and create_time_day='2018-04-%s'
    and user_id in (%s)
    group by create_time_day
    order by create_time_day"""%(day,userlist)
        cur.execute(sql)
        result = cur.fetchall()
        print result

    for j in range(7):
        dtime=day_t[i+j]
    #     sql="""select day,count(distinct uid)
    # from ssets_weblogs201
    # where roomid='123557'
    # and day='201804%s'
    # and uid>'0'
    # and cast(uid as int) in (select user_id
    # from stats_user_firstroom_v1
    # where room_id=123557
    # and create_time_day='2018-04-%s'
    # )
    # group by day"""%(dtime,day)
    #     cur.execute(sql)
    #     result=cur.fetchall()
    #     print result

    #     sql="""select create_time,count(distinct user_id)
    # from user_contribution
    # where create_time='2018-04-%s'
    # and room_id=123176
    # and behavior='behavior_send_gift'
    # and user_id in (%s)
    # group by create_time
    # order by create_time"""%(dtime,userlist)
    #     cursor = cnxn.cursor()
    #
    #     cursor.execute(sql)
    #     result = cursor.fetchall()
    #     print result


# cursor.close()
cnxn.close()
cur.close()
conn.close()