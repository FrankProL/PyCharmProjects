#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/4/8 11:06
# @Author  : Frank
# @Site    : 
# @File    : jingcai.py
# @Software: PyCharm
"""
import MySQLdb
import pandas as pd
from impala.dbapi import connect

from datetime import timedelta, datetime

yesterday = datetime.today() + timedelta(-1)
print (yesterday)
adate = yesterday.strftime('%Y-%m-%d')
bdate = yesterday.strftime('%Y%m%d')
# adate='2018-04-05'
# bdate='20180405'
print (adate, bdate)

print '开始查询mysql'
# 查询mysql  竞猜用户
into_db = ("rr-bp1mku8v6xlq45tpco.mysql.rds.aliyuncs.com", "loujianfeng", "FeTuH9bo6fakUw9", "utf8", "live_core")

cnxn = MySQLdb.connect(host=into_db[0], user=into_db[1], passwd=into_db[2], charset=into_db[3], db=into_db[4])

sql = """select t1.room_id,t2.nickname,t1.room_style,t1.user_id,t1.nickname,t1.create_time,t1.xnum,t1.money,t1.award
from (
  select r.room_id,r.anchor_id,r.room_style,r.user_id,s.nickname,s.create_time,r.xnum,r.money,r.award
  from 
  (
  select b.room_id,c.anchor_id,c.room_style,a.user_id,sum(a.xiazhu) as money,sum(a.rew) as award,sum(a.num) xnum
  from 
  (select user_id,question_id,sum(quizzes_amount) as xiazhu ,sum(reward_amount) as rew,count(user_id) as num 
  from jc_quiz
  GROUP BY user_id,question_id
  ORDER BY user_id,question_id
  ) as a ,
  (select id,room_id from jc_quiz_question where left(start_time,10)='%s') as b,
  anchor_room as c  
  where a.question_id=b.id and b.room_id=c.id
  group by b.room_id,c.anchor_id,c.room_style,a.user_id
  ORDER BY b.room_id
  ) as r left join 
  user as s
  on r.user_id=s.id
  order by r.room_id,r.user_id
) as t1 
left join 
user as t2 
on t1.anchor_id=t2.id """ % (adate)

cursor = cnxn.cursor()

cursor.execute(sql)
result = cursor.fetchall()
if result:
    df = pd.DataFrame(list(result))
    df.columns = [u'房间ID', u'主播昵称', u'房间类型', u'用户ID', u'昵称', u'注册时间', u'押注次数', u'押注金币累计', u'返还金币累计']
    print df  # .sort_values(by=0)
    user_id = list(df[u'用户ID'])
    print user_id
    print type(user_id)

    userlist = ','.join(map(str, user_id))
    print userlist

    placeholder = '?'  # For SQLite. See DBAPI paramstyle.
    placeholders = ', '.join(placeholder for unused in user_id)
    print placeholders
else:
    print result

cursor.close()
cnxn.close()

# ---------查询竞猜用户累计充值和当日充值金额---------------
if result:
    conn = connect(host='lg-15-163.ko.cn', port=21050)
    cur = conn.cursor()

    sql = """select user_id,sum(recharge_money) as historyrecharge
     from stats_user_recharge_v1
     where recharge_money>0
     and create_time_day<='%s'
     and user_id in (%s)
     group by user_id""" % (adate, userlist)
    cur.execute(sql)
    result = cur.fetchall()
    if result:
        df_history = pd.DataFrame(list(result))
        df_history.columns = [u'用户ID', u'用户累计充值']
        print df_history
        new = pd.merge(df, df_history, on=u'用户ID', suffixes=('', '_r'),
                       how='left')  # .join(df_day,on=u'用户ID',rsuffix='_rr')
    else:
        print result

    sql = """select user_id,sum(recharge_money) as dayrecharge
     from stats_user_recharge_v1
     where recharge_money>0
     and create_time_day='%s'
     and user_id in (%s)
     group by user_id""" % (adate, placeholders)
    cur.execute(sql, user_id)
    result = cur.fetchall()
    if result:
        df_day = pd.DataFrame(list(result))
        df_day.columns = [u'用户ID', u'用户当日充值']
        print df_day
        new_1 = pd.merge(new, df_day, on=u'用户ID', suffixes=('', '_rr'), how='left')
    else:
        print result
        new[u'用户当日充值'] = 0
        new_1 = new

    cur.close()
    conn.close()

    new_result = new_1[
        [u'房间ID', u'主播昵称', u'房间类型', u'用户ID', u'昵称', u'注册时间', u'用户累计充值', u'用户当日充值', u'押注次数', u'押注金币累计', u'返还金币累计']]
    print new_result
    tag=True
else:
    tag=False
if tag:
    new_result.to_excel('%s.xlsx'%(bdate), u'竞猜用户', float_format='%.5f',index=False)  # float_format 控制精度

