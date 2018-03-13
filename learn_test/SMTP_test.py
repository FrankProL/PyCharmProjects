#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/2/24 15:47
# @Author  : Frank
# @Site    : 
# @File    : SMTP_test.py
# @Software: PyCharm
"""
"""发送邮件
   http://blog.csdn.net/xiaosongbk/article/details/60142996
   http://www.runoob.com/python/python-email.html
"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "mail.dawang.tv"  # 设置服务器
mail_user = "loujianfeng@dawang.tv"  # 用户名
mail_pass = "NKv9q4k;2"  # 口令

sender = 'loujianfeng@dawang.tv'
receivers = ['loujianfeng@kong.net']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("ceshi", 'utf-8')
message['To'] = Header("测试", 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "邮件发送成功"
except smtplib.SMTPException:
    print "Error: 无法发送邮件"

