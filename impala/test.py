#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/3/5 11:27
# @Author  : Frank
# @Site    : 
# @File    : test.py.py
# @Software: PyCharm
"""
import MySQLdb
import pandas as pd
from impala.dbapi import connect

adate='2018-03-02'
bdate='20180302'

print '开始查询mysql'
# 查询mysql  竞猜用户
into_db = ("rr-bp1mku8v6xlq45tpco.mysql.rds.aliyuncs.com", "loujianfeng", "FeTuH9bo6fakUw9", "utf8","live_core")

cnxn = MySQLdb.connect(host=into_db[0], user=into_db[1], passwd=into_db[2], charset=into_db[3], db=into_db[4])

sql = """select DISTINCT r.room_id,r.user_id,s.nickname,s.create_time,r.xnum,r.money,r.award
from 
(
select b.room_id,a.user_id,sum(a.xiazhu) as money,sum(a.rew) as award,sum(a.num) xnum
from 
(select user_id,question_id,sum(quizzes_amount) as xiazhu ,sum(reward_amount) as rew,count(user_id) as num 
from jc_quiz
where left(quiz_time,10)='%s'
GROUP BY user_id,question_id
ORDER BY user_id,question_id
) as a ,
(select id,room_id from jc_quiz_question where left(start_time,10)='%s') as b 
where a.question_id=b.id
group by b.room_id,a.user_id
ORDER BY b.room_id
) as r left join 
user as s
on r.user_id=s.id
order by r.room_id,r.user_id;""" % (adate,adate)

cursor = cnxn.cursor()

cursor.execute(sql)
result=cursor.fetchall()
if result:
    df = pd.DataFrame(list(result))
    df.columns = [u'房间ID', u'用户ID', u'昵称', u'注册时间', u'押注次数', u'押注金币累计', u'返还金币累计']
    print df  #.sort_values(by=0)
    user_id=list(df[u'用户ID'])
    print user_id
    print type(user_id)

    userlist=','.join(map(str, user_id))
    print userlist

    placeholder = '?'  # For SQLite. See DBAPI paramstyle.
    placeholders = ', '.join(placeholder for unused in user_id)
    print placeholders
else:
    print result

cursor.close()
cnxn.close()




conn = connect(host='lg-15-163.ko.cn',port=21050)
cur = conn.cursor()

sql="""select user_id,sum(recharge_money) as historyrecharge
 from stats_user_recharge_v1
 where recharge_money>0
 and create_time_day<='%s'
 and user_id in (%s)
 group by user_id""" % (bdate,userlist)
cur.execute(sql)
result=cur.fetchall()
if result:
    df_history = pd.DataFrame(list(result))
    df_history.columns = [u'用户ID', u'用户累计充值']
    print df_history
else:
    print result

sql="""select user_id,sum(recharge_money) as historyrecharge
 from stats_user_recharge_v1
 where recharge_money>0
 and create_time_day='%s'
 and user_id in (%s)
 group by user_id""" % (adate,placeholders)
cur.execute(sql,user_id)
result=cur.fetchall()
if result:
    df_day = pd.DataFrame(list(result))
    df_day.columns = [u'用户ID', u'用户当日充值']
    print df_day
else:
    print result

cur.close()
conn.close()

new=pd.merge(df,df_history,on=u'用户ID',suffixes=('','_r'),how='left' )#.join(df_day,on=u'用户ID',rsuffix='_rr')
new_1=pd.merge(new,df_day,on=u'用户ID',suffixes=('','_rr'),how='left' )
print new_1
new_result= new_1[[u'房间ID', u'用户ID', u'昵称', u'注册时间',u'用户累计充值', u'用户当日充值', u'押注次数', u'押注金币累计', u'返还金币累计']]

"""写入excel"""
# create and writer pd.DataFrame to excel
# writer = pd.ExcelWriter('/home/none_pass/jingcai_activity_0213/Save_Excel.xlsx')      # linux 服务器路径
writer = pd.ExcelWriter('Save_Excel.xlsx')                                              # windows 运行路径
# writer.save()
"""写入excel"""
new_result.to_excel(writer, u'竞猜用户', float_format='%.5f')  # float_format 控制精度
writer.save()
writer.close()