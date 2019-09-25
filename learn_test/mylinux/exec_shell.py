#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/9/16 15:31
# @Author  : Frank
# @Site    : 
# @File    : exec_shell.py
# @Software: PyCharm
"""
import time
# 拼接多个子进程
import subprocess
child1 = subprocess.Popen(["ls","-l"], stdout=subprocess.PIPE)
child2 = subprocess.Popen(["wc"], stdin=child1.stdout,stdout=subprocess.PIPE)
out = child2.communicate()
print(out)

# 获取ext3对应的uuid
child = subprocess.Popen(["lsblk", "-f"], stdout=subprocess.PIPE)
out = child.stdout.readlines()
swap_uuid = None
for item in out:
    line = item.strip().split()
    print(len(line))
    if len(line) == 4:
        print(line[1])
        if(line[1] == b'ext3'):
            swap_uuid = line[2]
print(swap_uuid)

child=subprocess.Popen("yarn application -list |awk '{print $1,$2}'| grep application",shell=True,stdout=subprocess.PIPE)
out=child.stdout.readlines()
result_dict={}
for item in out:
    line=item.split()
    app_id=line[0]
    app_name=line[1]
    #print("app_id: "+app_id+" app_name: "+app_name)
    cmd="yarn application -status "+app_id+"|grep 'Start-Time' | awk -F ':' '{print $2}'"
    child_time=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
    start_time=child_time.communicate()[0].strip()
    now_mt = lambda: int(time.time() * 1000)
    task_time=(now_mt()-int(start_time))*1.0/60000
    #print(task_time)
    result_dict[app_id]=(app_name,task_time)
print(time.strftime('%Y-%m-%d %H:%M:%S'))
print("================================task time >10 :")
for key,value in result_dict.items():
    app_id=key
    app_name=value[0]
    task_time=value[1]
    if(task_time>5):
        print("   yarn application -kill " + key + "   " + value[0] + "    " + str(value[1]))
        subprocess.Popen("yarn application -kill "+key,shell=True)
print("================================hour task and time >5 :")
for key,value in result_dict.items():
    # print("yarn application -kill " + key + "   " + value[0] + "    " + str(value[1]))
    app_id=key
    app_name=value[0]
    task_time=value[1]
    if("hour" in app_name and task_time>1):
        print("   yarn application -kill " + key + "   " + value[0] + "    " + str(value[1]))
#for key,value in result_dict.items():
#    print("yarn application -kill " + key + "   " + value[0] + "    " + str(value[1]))

