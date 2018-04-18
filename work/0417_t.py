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

conn = connect(host='lg-15-163.ko.cn', port=21050)
cur = conn.cursor()

data = pd.read_csv('tmp_data.csv', header=None)
data.columns = ['uid']
days=['06','07','08','09','10','11','12','13','14','15']
for i in range(6, 16):
    dataX = pd.read_csv('tmp_data_%s.csv' % i, header=None)
    dataX.columns = ['uid%s' % i]
    day=days[i-6]

    dd = pd.merge(dataX, data, left_on='uid%s' % i, right_on='uid', how='left')

    print ('----------------------%s 号--房间访问用户中是直播间新增用户的用户数------------------------'%i)
    # print len(dd[pd.isnull(dd['uid'])]['uid%s' % i])

    user_id = list(dd[pd.isnull(dd['uid'])]['uid%s' % i])
    userlist = ','.join(map(str, user_id))
    # print user_id

    sql = """select user_id
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


#     sql = """select create_time_day,sum(recharge_gold) as gold ,count(distinct user_id) as num
# from stats_user_recharge_v1
# where recharge_gold>0
# and create_time_day='2018-04-%s'
# and user_id in (%s)
# group by create_time_day
# order by create_time_day"""%(day,userlist)
#     cur.execute(sql)
#     result = cur.fetchall()
#     print result

    sql="""select channel_id,count(id)
from stats_user_base_v1
where id in (%s)
group by channel_id
order by channel_id"""%(userlist)
    cur.execute(sql)
    result=cur.fetchall()
    print pd.DataFrame(result)

#     sql="""select user_id
# from stats_user_firstroom_v1
# where room_id=123557
# and create_time_day='2018-04-06'"""
#     cur.execute(sql)
#     result=cur.fetchall()
#     print len(result)
#     tmp=pd.DataFrame(result)
#     tmp.columns=['user_id']
#     new=pd.merge(dd[pd.isnull(dd['uid'])],tmp,left_on='uid%s'%i,right_on='user_id',how='outer')
#     print new


    # print ('----------------------------------------------')
    # print len(data['uid'])
    dataX.columns = ['uid']
    data = data.append(dataX)
    data = data.drop_duplicates()
    # print len(data['uid'])
    # print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
cur.close()
conn.close()