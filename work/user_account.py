#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/3/21 9:44
# @Author  : Frank
# @Site    : 
# @File    : user_account.py
# @Software: PyCharm
"""
import MySQLdb
import chardet
from impala.dbapi import connect
import pandas as pd


with open("rank.csv") as f:
    data = []
    # data=f.readlines()
    for line in f:
        line=line.strip('\n')
        data.append(line)
print data

into_db = ("rr-bp1mku8v6xlq45tpco.mysql.rds.aliyuncs.com", "loujianfeng", "FeTuH9bo6fakUw9", "utf8","live_core")

cnxn = MySQLdb.connect(host=into_db[0], user=into_db[1], passwd=into_db[2], charset=into_db[3], db=into_db[4])

sql = """SELECT a.user_id,b.nickname,b.user_rank,'' as rank,a.gold,a.diamond
from dw_user_account as a
left join
   user as b on a.user_id=b.id
where a.gold>0 or a.diamond>0
"""

cursor = cnxn.cursor()

cursor.execute(sql)
result=cursor.fetchall()
if result:
    df = pd.DataFrame(list(result))
    df.columns = ['user_id', 'nickname', 'user_rank','rank', 'gold', 'diamond']

    user_id=list(df['user_id'])

    rank={}
    df['user_rank']=int(df['user_rank'])
    for index,row in df.iterrows():
        rank.setdefault(index,0)
        rank[index]=data[row['user_rank']-1]
        # df['rank'][index]=data[int(row['user_rank']-1)]
        # print chardet.detect(row['rank'])
    df['rank']=rank.values()

    print df['rank'],

cursor.close()
cnxn.close()

print ('=================================================')

conn = connect(host='lg-15-163.ko.cn',port=21050)
cur = conn.cursor()

sql="""select distinct uid,'1' as log1
from ssets_weblogs201
where month='201803'"""
cur.execute(sql)
result=cur.fetchall()
# print result
cur.close()
conn.close()

if result:
    df_log = pd.DataFrame(list(result))
    df_log.columns = ['user_id', 'log1']
    new = pd.merge(df, df_log, on='user_id', suffixes=('', '_r'), how='left')


print ('=================================================')

conn = connect(host='lg-15-163.ko.cn',port=21050)
cur = conn.cursor()

sql="""select distinct uid,'1' as log1
from ssets_weblogs201
where month>='201801' and month<='201803'"""
cur.execute(sql)
result=cur.fetchall()
# print result
cur.close()
conn.close()

if result:
    df_log2 = pd.DataFrame(list(result))
    df_log2.columns = ['user_id', 'log1']
    new2 = pd.merge(new, df_log2, on='user_id', suffixes=('', '_r'), how='left')

new2=new2.fillna(0)
new2.to_csv('result.csv',index=False,sep=',',encoding='utf-8',)