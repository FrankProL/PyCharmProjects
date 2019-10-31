#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/10/31 11:28
# @Author  : Frank
# @Site    :
# @File    : kill_hive.py
# @Software: PyCharm
"""

import json
import subprocess
import urllib2
import sys
##rmIP地址
rmIpList = ('192.168.1.226', '192.168.1.227')
##获取JOB的API
rmUrl = 'http://%s:8088/ws/v1/cluster/apps?state=running'
##超时KILL时间(秒)
timeout = 3600

##获取app
def getAppsList(rmUrl):
    response = urllib2.urlopen(rmUrl)
    appList = response.read()
    if json.loads(appList)['apps'] == None:
        return None
    else:
        return json.loads(appList)['apps']['app']

if __name__ == '__main__':
    try:
        appList=getAppsList(rmUrl % rmIpList[0])
    except:
        appList=getAppsList(rmUrl % rmIpList[1])
    if appList==None:
        print("========no running task============")
        sys.exit(0)
    print("===============all task=======================")
    for app in appList:
        print 'yarn application -kill '+app['id']+'     '+app['name']+'     '+str(app['elapsedTime']*1.0/60000)
    print("================print other user==============================")
    for app in appList:
        if "root.root" not in app['queue'] and "root.hdfs" not in app['queue']:
            print 'yarn application -kill ' + app['id'] + '     ' + app['queue'] + '     ' + str(
                app['elapsedTime'] * 1.0 / 60000)+'   '+ app['name']
    print("================kill hive on spark==============================")
    for app in appList:
        if "Hive" in app['name']:
            subprocess.call("yarn application -kill "+app['id'],shell=True)








