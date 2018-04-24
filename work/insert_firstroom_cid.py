#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/4/24 10:59
# @Author  : Frank
# @Site    : 
# @File    : insert_firstroom_cid.py
# @Software: PyCharm
"""
from impala.dbapi import connect
from datetime import timedelta, datetime

yesterday = datetime.today() + timedelta(-1)
print (yesterday)
adate = yesterday.strftime('%Y-%m-%d')
bdate = yesterday.strftime('%Y%m%d')
print (adate + ' ----- ' + bdate)

"""发送报警邮件"""
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
subject = '房间首次登陆及cid'
message['Subject'] = Header(subject, 'utf-8')

conn = connect(host='lg-15-163.ko.cn', port=21050)
cur = conn.cursor()

sql = """insert into stats_user_firstroom_v1
select id,user_id,room_id,create_time,
substring(create_time,1,4) as create_time_year,
substring(create_time,1,7) as create_time_month,
substring(create_time,1,10) as create_time_day
from(select concat(uid,"-",substring(roomid,1,6)) as id, cast(uid as bigint) as user_id,cast(substring(roomid,1,6) as bigint) as room_id,min(datatime) as create_time
  from ssets_weblogs201
  where  roomid is not null
  and roomid <> ''
  and uid>'0'
  and day='%s'
  group by uid,roomid) a	""" % (bdate)

try:
    cur.execute(sql)
    print ('%s日房间首次登陆用户插入成功' % adate)
except:
    try:
        message.attach(MIMEText('房间首次登陆插入数据失败：(自动发送)', 'plain', 'utf-8'))
        smtpObj = smtplib.SMTP(mail_host)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print ("数据插入失败，报警邮件已发送")
    except smtplib.SMTPException:
        print ("Error: 无法发送邮件")

sql = """insert into stats_app_firstcid_v1
select a.cid,platformflag,channelid,substring(channelid,1,4),system_version,device,client_version,netoperator,manufacturer,idfa,datatime,
  substring(datatime,1,4),substring(datatime,1,7),substring(datatime,1,10) 
from  ssets_logs210_app a 
left join (select cid, min(datatime) dt 
            from ssets_logs210_app 
			where day='%s' group by cid) b 
on b.cid=a.cid and a.datatime = b.dt 
where a.day='%s' and b.cid is not null;""" % (bdate, bdate)

try:
    cur.execute(sql)
    print('%s日cid数据插入成功' % adate)
except:
    try:
        message.attach(MIMEText('cid插入数据失败：(自动发送)', 'plain', 'utf-8'))
        smtpObj = smtplib.SMTP(mail_host)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print ("数据插入失败，报警邮件已发送")
    except smtplib.SMTPException:
        print ("Error: 无法发送邮件")

cur.close()
conn.close()
