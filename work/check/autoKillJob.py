#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/10/16 18:36
# @Author  : Frank
# @Site    : 
# @File    : autoKillJob.py
# @Software: PyCharm
"""

'''
每小时定时查杀1小时以上的任务
crontab 0 * * * *
Author: 杨松

init_cmd: mkdir -p  /usr/local/scripts/hadoop_util
'''

'''
建表语句

drop table bigdata_hadoop_autokill_config;
create table bigdata_hadoop_autokill_config(
        id bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'ID',
        app_name varchar(50) comment '任务名称(app_name)',
        isTrue char(1) default 'Y' comment '是否生效(Y N)',
        PRIMARY KEY (`id`)
) COMMENT='超长任务查杀白名单' ;

'''
import time
import urllib2
import json
import sys
import os
import commands

##rmIP地址
rmIpList = ('192.168.1.226', '192.168.1.227')
##获取JOB的API
rmUrl = 'http://%s:8088/ws/v1/cluster/apps?state=running'
##超时KILL时间(秒)
timeout = 3600

##kill user list
killUserList = ['root', 'hdfs']

##mysql信息
mysql_ip = '192.168.1.208'
mysql_port = '3306'
mysql_username = 'basicstat'
mysql_pass = 'basicstatpassword'
mysql_dbname = 'basicstat'


##获取app
def getAppsList(rmUrl):
    response = urllib2.urlopen(rmUrl)
    appList = response.read()
    if json.loads(appList)['apps'] == None:
        return None
    else:
        return json.loads(appList)['apps']['app']


##get
def getKillRule():
    '''
    db = pymysql.connect(mysql_ip, mysql_username, mysql_pass, mysql_dbname,charset='utf8')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "SELECT APP_NAME FROM bigdata_hadoop_autokill_config WHERE ISTRUE='Y'"
    # 执行SQL语句
    cursor.execute(sql)
    result = cursor.fetchall()
    '''

    result = ['sqoop_export_', 'c_channel_roi_', 'shafa_chid_users_ref_day_']
    return result


##过滤sd

if __name__ == '__main__':
    f = open('/var/log/hadoop_ops.log', 'aw')
    try:
        appList = getAppsList(rmUrl % rmIpList[0])
    except:
        appList = getAppsList(rmUrl % rmIpList[1])
    if appList == None:
        f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' 无数据\n')
        sys.exit(0)
    ruleList = getKillRule()
    f.write('KillRule:' + str(ruleList) + '\n')
    for i in appList:

        if i['elapsedTime'] > 1000 * timeout:
            cnt = 0
            for tmp in ruleList:
                if not str(i['name']).find(tmp) == -1:
                    cnt = cnt + 1
                    break
            if cnt == 0 and i['user'] in killUserList:
                f.write(
                    time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' ' + i['user'] + ' ' + i['name'] + ' ' + i[
                        'id'] + ' ' + ' need to kill\n')

                (status, output) = commands.getstatusoutput('yarn application -kill %s' % i['id'])

                f.write(time.strftime("%Y-%m-%d %H:%M:%S",
                                      time.localtime()) + '========================== yarn application kill start =========================\n')
                f.write('status:' + str(status) + '\n')
                f.write(output + '\n')
                f.write(time.strftime("%Y-%m-%d %H:%M:%S",
                                      time.localtime()) + '=========================== yarn application kill end   ========================\n')

    f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' done\n')
    f.close()