#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/3/16 15:39
# @Author  : Frank
# @Site    : 
# @File    : spark_read.py
# @Software: PyCharm
"""
from collections import defaultdict
from impala.dbapi import connect
"""
    统计用户发言中包含敏感词的条数、和用户数
"""

with open("sensitive_words.txt") as f:
    data =[]
    for line in f:
        line = line.strip('\n')
        data.append(line.decode('gbk').encode('utf-8'))
    # print data
    # for str in data:
    #     print str
    #     print len(str)


conn = connect(host='lg-15-163.ko.cn',port=21050)
cur = conn.cursor()

sql="""select uid,msg from ssets_chatmsg201 where day='20180315'"""
cur.execute(sql)
result=cur.fetchall()
# print result
cur.close()
conn.close()

user=set()
num=0
i=0
d = defaultdict(list)
for k,v in result:
    for s in data:
        if s in v:
            print s,'\t-->',v
            user.add(k)
            num+=1
    d[k].append(v)
    i+=1
    # if i>1000:
    #     break
# print (d.items())
# print (type(d))
# print d.keys()
# print d.values()
print len(user),num


