#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/2 19:18
# @Author  : Frank
# @Site    : 
# @File    : spark_read.py
# @Software: PyCharm
"""
# import os
# from ipip import IP
# from ipip import IPX
#
#
# IP.load(os.path.abspath("mydata4vipday2.dat"))
# print IP.find("118.28.8.8")
#
# IPX.load(os.path.abspath("mydata4vipday2.datx"))
# print IPX.find("118.28.8.8")
import MySQLdb
import datx

# 查询地级市精度的IP库


c = datx.City("mydata4vipweek2.dat")
print(c.find("8.8.8.258"))
print(c.find("255.255.255.255"))
# print(c.find('192.168.101.126'))

# # 查询国内区县库
# d = datx.District("/path/to/quxian.datx")
# print(d.find("123.121.117.72"))
#
# # 查询基站IP库
# d = datx.BaseStation("/path/to/station_ip.datx")
# print(d.find("223.221.121.0"))

"""http://ip.taobao.com/service/getIpInfo2.php?ip="""

# # 查询mysql
# into_db = ("172.23.15.8", "kuanghao", "kju3kj0d", "utf8","logtest")
# cnxn = MySQLdb.connect(host=into_db[0], user=into_db[1], passwd=into_db[2], charset=into_db[3], db=into_db[4])
# cursor = cnxn.cursor()
# sql=""""""
# cursor.execute(sql)
# result=cursor.fetchall()
# cursor.close()
# cnxn.close()
import time
import requests


def writefile(L=[]):
    with open('ip_addr.txt', 'a') as f:
        for s in L:
            f.write(s)
            f.write('\n')                           # 多写一个空行。。。读文件时麻烦。。。。
        f.close()


headers = {'Host': 'ip.taobao.com',
           'Referer': 'http://ip.taobao.com/ipSearch.html',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
           }
l = []
with open('ip.txt', 'r') as ipfile:
    for line in ipfile:
        ip = line
        # print ip
        url = 'http://ip.taobao.com/service/getIpInfo2.php?ip=' + ip
        with requests.get(url,headers=headers)as f:             # linux中，此处报错，无法运行
            data = f.content
            # print data
            l.append(data)
            if len(l) > 100:
                print (data)
                writefile(l)
                l = []
        time.sleep(0.2)
