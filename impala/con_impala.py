#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/2/23 9:24
# @Author  : Frank
# @Site    : 
# @File    : con_impala.py
# @Software: PyCharm
"""
import pandas as pd
import MySQLdb
from impala.dbapi import connect

from datetime import timedelta, datetime

yesterday = datetime.today() + timedelta(-1)
print yesterday
adate = yesterday.strftime('%Y-%m-%d')
bdate = yesterday.strftime('%Y%m%d')
print adate,bdate

# adate='2018-02-09'
# bdate='20180209'

# adate='2018-02-14'
# bdate='20180214'

# 查询mysql  竞猜题目数
into_db = ("rr-bp1o90m39oporf1g1o.mysql.rds.aliyuncs.com", "loujianfeng", "FeTuH9bo6fakUw9", "utf8","live_core")

cnxn = MySQLdb.connect(host=into_db[0], user=into_db[1], passwd=into_db[2], charset=into_db[3], db=into_db[4])

sql = """select room_id,count(id) from jc_quiz_question 
where left(start_time,10)='%s' group by room_id""" % (adate)

cursor = cnxn.cursor()

cursor.execute(sql)
result=cursor.fetchall()
print (result)
if not result:
    print "result is null"
    _20, _21, _22=0,0,0
else:
    if len(result) == 1:
        if result[0][0] == 123269:
            _20 = result[0][1]
            _21 = result[0][1]
            _22 = 0
        else:
            _20 = result[0][1]
            _21 = 0
            _22 = result[0][1]
    else:
        if result[0][0] == 123269:
            _20 = result[0][1] + result[1][1]
            _21 = result[0][1]
            _22 = result[1][1]
        else:
            _20 = result[0][1] + result[1][1]
            _21 = result[1][1]
            _22 = result[0][1]
print type(result)

print _20,_21,_22


cursor.close()
cnxn.close()


conn = connect(host='lg-15-163.ko.cn',port=21050)
cur = conn.cursor()

# 历史首次充值人数	历史首次充值用户充值金额
cur.execute("""SELECT COUNT(DISTINCT user_id),SUM(recharge_money) from stats_user_recharge_v1 where recharge_money>0 and create_time_day='%s'
and user_id not in
(
SELECT DISTINCT user_id
from stats_user_recharge_v1
where create_time_day<'%s' and recharge_money>0
)""" % (adate,adate))
result=cur.fetchone()
_00=result[0]
_10=result[1]
print _00,_10


# 房间登录用户数
sql="""select roomid,count(distinct uid)
from ssets_weblogs201
where day='%s'
and roomid in ('123269','124770')
group by roomid""" % (bdate)
cur.execute(sql)
result=cur.fetchall()
print result
if result[0][0]==123269:
    _31=result[0][1]
    _32=result[1][1]
else:
    _31=result[1][1]
    _32=result[0][1]
print _31,_32


# 123269房间登录用户充值人数
sql="""select count(distinct user_id)
from stats_user_recharge_v1
where recharge_money>0 and create_time_day='%s'
and user_id in (select distinct cast(trim(uid) as bigint)
from ssets_weblogs201
where day='%s'
and roomid='123269')""" % (adate,bdate)
cur.execute(sql)
result=cur.fetchone()
print result
_41=result[0]
print _41


# 124770房间登录用户充值人数
sql="""select count(distinct user_id)
from stats_user_recharge_v1
where recharge_money>0 and create_time_day='%s'
and user_id in (select distinct cast(trim(uid) as bigint)
from ssets_weblogs201
where day='%s'
and roomid='124770')""" % (adate,bdate)
cur.execute(sql)
result=cur.fetchone()
print result
_42=result[0]
print _42


# 123269房间登录用户充值金额（去除红星闪闪）
sql="""select sum(recharge_money)
from stats_user_recharge_v1
where recharge_money>0 and create_time_day='%s'
and user_id in (select distinct cast(trim(uid) as bigint)
from ssets_weblogs201
where day='%s'
and roomid='123269')
and user_id<>20002130""" % (adate,bdate)
cur.execute(sql)
result=cur.fetchone()
print result
_51=result[0]
print _51


# 124770房间登录用户充值金额（去除红星闪闪）
sql="""select sum(recharge_money)
from stats_user_recharge_v1
where recharge_money>0 and create_time_day='%s'
and user_id in (select distinct cast(trim(uid) as bigint)
from ssets_weblogs201
where day='%s'
and roomid='124770')
and user_id<>20002130""" % (adate,bdate)
cur.execute(sql)
result=cur.fetchone()
print result
_52=result[0]
print _52


# 123269房间登录用户首次充值人数
sql="""SELECT COUNT(DISTINCT user_id)
from stats_user_recharge_v1
where recharge_money>0 and create_time_day='%s'
and user_id not in
(
SELECT DISTINCT user_id
from stats_user_recharge_v1
where create_time_day<'%s' and recharge_money>0
)
and user_id in (select distinct cast(trim(uid) as bigint)
from ssets_weblogs201
where day='%s'
and roomid='123269')""" % (adate,adate,bdate)
cur.execute(sql)
result=cur.fetchone()
print result
_61=result[0]
print _61


# 124770房间登录用户首次充值人数
sql="""SELECT COUNT(DISTINCT user_id)
from stats_user_recharge_v1
where recharge_money>0 and create_time_day='%s'
and user_id not in
(
SELECT DISTINCT user_id
from stats_user_recharge_v1
where create_time_day<'%s' and recharge_money>0
)
and user_id in (select distinct cast(trim(uid) as bigint)
from ssets_weblogs201
where day='%s'
and roomid='124770')""" % (adate,adate,bdate)
cur.execute(sql)
result=cur.fetchone()
print result
_62=result[0]
print _62


# 123269房间登录用户首次充值金额
sql="""select sum(b.recharge_money)
from
(
  select a.user_id,sum(a.recharge_money) as recharge_money
  from
  (
    select user_id,create_time_day,recharge_money,row_number() over (partition by user_id order by create_time) as row_number from stats_user_recharge_v1 where recharge_money>0
  ) a
  where a.row_number =1 and a.create_time_day = '%s' group by a.user_id
) b
where b.user_id in (select distinct cast(trim(uid) as bigint)
from ssets_weblogs201
where day='%s'
and roomid='123269')""" % (adate,bdate)
cur.execute(sql)
result=cur.fetchone()
print result
_71=result[0]
print _71


# 124770房间登录用户首次充值金额
sql="""select sum(b.recharge_money)
from
(
  select a.user_id,sum(a.recharge_money) as recharge_money
  from
  (
    select user_id,create_time_day,recharge_money,row_number() over (partition by user_id order by create_time) as row_number from stats_user_recharge_v1 where recharge_money>0
  ) a
  where a.row_number =1 and a.create_time_day = '%s' group by a.user_id
) b
where b.user_id in (select distinct cast(trim(uid) as bigint)
from ssets_weblogs201
where day='%s'
and roomid='124770')""" % (adate,bdate)
cur.execute(sql)
result=cur.fetchone()
print result
_72=result[0]
print _72


# 123269房间登录用户数新增注册人数
sql="""select count(id)
from stats_user_base_v1
where create_time_day='%s'
and id in (select distinct cast(trim(uid) as bigint)
from ssets_weblogs201
where day='%s'
and roomid='123269')""" % (adate,bdate)
cur.execute(sql)
result=cur.fetchone()
print result
_81=result[0]
print _81


# 124770房间登录用户数新增注册人数
sql="""select count(id)
from stats_user_base_v1
where create_time_day='%s'
and id in (select distinct cast(trim(uid) as bigint)
from ssets_weblogs201
where day='%s'
and roomid='124770')""" % (adate,bdate)
cur.execute(sql)
result=cur.fetchone()
print result
_82=result[0]
print _82


# 123269房间登录用户数新增注册充值人数	房间登录用户数新增注册充值金额
sql="""SELECT COUNT(DISTINCT user_id),SUM(recharge_money)
from stats_user_recharge_v1
where recharge_money>0 and create_time_day='%s'
and user_id in
(
select id
from stats_user_base_v1
where create_time_day='%s'
and id in (select distinct cast(trim(uid) as bigint)
from ssets_weblogs201
where day='%s'
and roomid='123269')
)""" % (adate,adate,bdate)
cur.execute(sql)
result=cur.fetchone()
print result
_91=result[0]
_101=result[1]
print _91,_101


# 124770房间登录用户数新增注册充值人数	房间登录用户数新增注册充值金额
sql="""SELECT COUNT(DISTINCT user_id),SUM(recharge_money)
from stats_user_recharge_v1
where recharge_money>0 and create_time_day='%s'
and user_id in
(
select id
from stats_user_base_v1
where create_time_day='%s'
and id in (select distinct cast(trim(uid) as bigint)
from ssets_weblogs201
where day='%s'
and roomid='124770')
)""" % (adate,adate,bdate)
cur.execute(sql)
result=cur.fetchone()
print result
_92=result[0]
_102=result[1]
print _92,_102

cur.close()
conn.close()

data=[[_00,u'----',u'----'],
[_10,u'----',u'----'],
[_20,_21,_22],
[u'----',_31,_32],
[u'----',_41,_42],
[u'----',_51,_52],
[u'----',_61,_62],
[u'----',_71,_72],
[u'----',_81,_82],
[u'----',_91,_92],
[u'----',_101,_102]]
print data


# print '开始查询mysql'
# # 查询mysql  竞猜用户
# into_db = ("rr-bp1o90m39oporf1g1o.mysql.rds.aliyuncs.com", "loujianfeng", "FeTuH9bo6fakUw9", "utf8","live_core")
#
# cnxn = MySQLdb.connect(host=into_db[0], user=into_db[1], passwd=into_db[2], charset=into_db[3], db=into_db[4])
#
# sql = """select DISTINCT r.room_id,r.user_id,s.nickname,s.create_time,t.historyrecharge,u.recharge,r.xnum,r.recharge_money,r.award
# from
# (
# select b.room_id,a.user_id,sum(a.xiazhu) as recharge_money,sum(a.rew) as award,sum(a.num) xnum
# from
# (select user_id,question_id,sum(quizzes_amount) as xiazhu ,sum(reward_amount) as rew,count(user_id) as num
# from jc_quiz
# where left(quiz_time,10)='%s'
# GROUP BY user_id,question_id
# ORDER BY user_id,question_id
# ) as a ,
# (select id,room_id from jc_quiz_question where left(start_time,10)='%s') as b
# where a.question_id=b.id
# group by b.room_id,a.user_id
# ORDER BY b.room_id
# ) as r left join
# user as s
# on r.user_id=s.id
# left join (select user_id,sum(recharge_money) as historyrecharge
#  from user_account_log
#  where recharge_money>0
#  and DATE(create_time)<='%s'
#  group by user_id ) as t on r.user_id=t.user_id
# left join (select user_id,sum(recharge_money) as recharge
#  from user_account_log
#  where recharge_money>0
#  and DATE(create_time)='%s'
#  group by user_id ) as u on r.user_id=u.user_id
# order by r.room_id,r.user_id""" % (adate,adate,adate,adate)
#
# cursor = cnxn.cursor()
#
# cursor.execute(sql)
# result=cursor.fetchall()
# print (result)
# print type(result)
#
# cursor.close()
# cnxn.close()


"""写入excel"""
data_df = pd.DataFrame(data)

title_1= yesterday.strftime('%m-%d')
title_2= yesterday.strftime('%m-%d(123269)')
title_3= yesterday.strftime('%m-%d(124770)')

# change the index and column name
data_df.columns = ['%s' % (title_1),'%s' % (title_2),'%s' % (title_3)]
data_df.index = [u'历史首次充值人数',u'历史首次充值用户充值金额(当天充值)',u'竞猜题目数',u'房间登录用户数',u'房间登录用户充值人数',u'房间登录用户充值金额（去除红星闪闪）',
                 u'房间登录用户首次充值人数',u'房间登录用户首次充值金额',u'房间登录用户数新增注册人数',u'房间登录用户数新增注册充值人数',u'房间登录用户数新增注册充值金额']

# create and writer pd.DataFrame to excel
writer = pd.ExcelWriter('/home/none_pass/jingcai_activity_0213/Save_Excel.xlsx')      # linux 服务器路径
# writer = pd.ExcelWriter('Save_Excel.xlsx')                                              # windows 运行路径
data_df.to_excel(writer,u'充值注册',float_format='%.5f') # float_format 控制精度

# # writer.save()
# """写入excel"""
# if result:
#     data_df_mysql = pd.DataFrame(list(result))
#
#     data_df_mysql.columns = [u'房间ID', u'用户ID', u'昵称', u'注册时间', u'充值累计', u'当天充值累计', u'押注次数', u'押注金币累计', u'返还金币累计']
#
#     data_df_mysql.to_excel(writer, u'竞猜用户', float_format='%.5f')  # float_format 控制精度
writer.save()
writer.close()

"""发送邮件"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# SMTP 服务
mail_host = "mail.dawang.tv"  # 设置服务器
mail_user = "loujianfeng@dawang.tv"  # 用户名
mail_pass = "NKv9q4k;2"  # 口令

sender = 'loujianfeng@dawang.tv'
receivers = ['loujianfeng@kong.net']

# 创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header("dawang.tv", 'utf-8')
message['To'] = Header("kong.net", 'utf-8')
subject = '竞猜活动'
message['Subject'] = Header(subject, 'utf-8')

# 邮件正文内容
message.attach(MIMEText('竞猜活动数据：(自动发送)', 'plain', 'utf-8'))

# 构造附件1，传送当前目录下的 test.txt 文件
att1 = MIMEText(open('/home/none_pass/jingcai_activity_0213/Save_Excel.xlsx', 'rb').read(), 'base64', 'utf-8')  # linux
# att1 = MIMEText(open('Save_Excel.xlsx', 'rb').read(), 'base64', 'utf-8')    # windows
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="Save_Excel.xlsx"'
message.attach(att1)

try:
    smtpObj = smtplib.SMTP(mail_host)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "邮件发送成功"
except smtplib.SMTPException:
    print "Error: 无法发送邮件"