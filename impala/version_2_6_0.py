#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/3/2 17:47
# @Author  : Frank
# @Site    : 
# @File    : version_2_6_0.py
# @Software: PyCharm
"""
import pandas as pd
import MySQLdb
from impala.dbapi import connect

adate='2018-03-01'
bdate='20180301'
# adate='2018-02-14'
# bdate='20180214'

# 查询mysql  2.6.0版本新增注册用户数
into_db = ("rr-bp1o90m39oporf1g1o.mysql.rds.aliyuncs.com", "loujianfeng", "FeTuH9bo6fakUw9", "utf8","live_core")

cnxn = MySQLdb.connect(host=into_db[0], user=into_db[1], passwd=into_db[2], charset=into_db[3], db=into_db[4])

sql = """select platform,count(id)
from dw_user
where left(create_time,10)='%s'
and client_version='2.6.0'
GROUP BY platform""" % (adate)

cursor = cnxn.cursor()

cursor.execute(sql)
result=cursor.fetchall()
print '2.6.0版本新增注册用户数'
print (result)

cursor.close()
cnxn.close()

"""=====================impala====================================="""
conn = connect(host='lg-15-163.ko.cn',port=21050)
cur = conn.cursor()

# 除2.6.0外版本的登录活跃
sql="""select platformflag,count(distinct uid)
from ssets_logs210_app
where day='%s'
and client_version<>'2.6.0'
and uid<>'0'
group by platformflag""" % (bdate)
cur.execute(sql)
result=cur.fetchall()
print '除2.6.0外版本的登录活跃'
print result

# 升级到2.6.0用户数
sql="""select platformflag,count(distinct uid)
from ssets_logs210_app
where day='%s'
and client_version='2.6.0'
and uid<>'0'
and uid not in (select distinct uid
 from ssets_logs210_app
 where day<'%s'
 and client_version='2.6.0'
 and uid<>'0'
)
group by platformflag""" % (bdate,bdate)
cur.execute(sql)
result=cur.fetchall()
print '升级到2.6.0用户数'
print result

# 未升级用户数
sql="""select platformflag,count(distinct uid)
from ssets_logs210_app
where day='%s'
and client_version<>'2.6.0'
and uid<>'0'
and uid not in (select distinct uid
 from ssets_logs210_app
 where day='%s'
 and client_version='2.6.0'
 and uid<>'0')
group by platformflag""" % (bdate,bdate)
cur.execute(sql)
result=cur.fetchall()
print '未升级用户数'
print result

# 2.6.0版本参与小游戏人数
sql="""select t1.platform,count(t1.user_id)
from 
(
select distinct user_id,platform
from stats_yuanyi_game_log_v1
where client_version='2.6.0'
and uri is not null 
and create_time_day='%s'
) as t1 join 
(
select distinct user_id
from stats_bean_consume_log_v1
where create_time_day='%s'
and game_manu_id>'0'
) as t2 
where t1.user_id=t2.user_id
group by t1.platform""" % (adate,adate)
cur.execute(sql)
result=cur.fetchall()
print '2.6.0版本参与小游戏人数'
print result

cur.close()
conn.close()