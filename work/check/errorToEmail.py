#!/usr/bin/env python
# coding=utf-8
#Author: tiger.L
#Date: 2018/6/13

import logging
import time
import os
import sys
import codecs
import smtplib
from email.mime.text import MIMEText
from email.header import Header
reload(sys)
sys.setdefaultencoding('utf-8')


def output_log(level, info):
    """
    定义日志输出样式
    :param level: 
    :param info: 
    :return: 
    """
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='/var/log/errortoemail.log',
                        filemode='a')
    if level == "debug":
        logging.debug(info)
    elif level == "error":
        logging.error(info)
    elif level == "warning":
        logging.warning(info)
    else:
        logging.info(info)


def get_mailto_list():
    receiver_list = []
    mailtolist = "/tmp/mailtolist.txt"
    wget_cmd = "wget http://gitlab.qcread.cn:5055/mailtolist.txt -O %s >/dev/null 2>&1" % mailtolist
    os.system(wget_cmd)
    if os.path.exists(mailtolist):
        f = open(mailtolist)
        name_list = f.readlines()
        for name in name_list:
            receiver_list.append(name.strip('\n'))
    else:
        output_log("warning", "未下载%s文件" % mailtolist)
        receiver_list = ['ligh@ishugui.com;', 'zhangfei@ishugui.com;', 'wangjc@ishugui.com;']

    return receiver_list


def send_mail(mail_msg):
    sender = 'warning@dianzhong.com'
    receiver = ['ligh@ishugui.com;', 'liangbl@ishugui.com;', 'yangsong@ishugui.com;']
    #receiver = ['ligh@ishugui.com;']
    output_log("info", "邮件接收人为：%s" % receiver)
    subject = "报表数据异常，请查看！" 
    smtpserver = 'smtp.exmail.qq.com'
    username = 'warning@dianzhong.com'
    password = 'Wn1234'
    email_text = mail_msg

    msg = MIMEText(email_text, _subtype='plain', _charset='utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = ";".join(receiver)

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    time.sleep(5)
    smtp.quit()


def get_date():
    year_month = time.strftime("%Y%m", time.localtime(time.time()))
    date_hour = time.strftime("%d_%H", time.localtime(time.time()))
    return year_month, date_hour


def get_log_file(log_type):
    if log_type == "CPS":
        date_now, hour_now = get_date()
        error_log = "/var/log/cpslog/%s/%s_error.log" % (date_now, hour_now)
    else:
        error_log = "/var/log/nginx/cps_error.log"
    output_log("info", "error_log_file is %s" % error_log)
    return error_log


def get_last_log(log_file):
    cmd = "cat %s" % log_file
    result = os.system(cmd)
    if result == 0:
        f = codecs.open(log_file, encoding='utf-8')
        mail_msg = "异常报表如下: \n"
        while True:
            line = f.readline()
            mail_msg += line.strip() + '\n'
            if not line:
                break
        f.close()
        send_mail(mail_msg)
    else:
        raise AssertionError("获取最新日志内容失败！")


if __name__ == "__main__":
    try:
        log_file = sys.argv[1]
        get_last_log(log_file)
    except Exception as msg:
        output_log("error", msg)
