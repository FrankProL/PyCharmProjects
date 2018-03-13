#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/2/27 18:02
# @Author  : Frank
# @Site    : 
# @File    : data.py
# @Software: PyCharm
"""
import pandas as pd
import MySQLdb
from impala.dbapi import connect
from datetime import timedelta, datetime

t = ['2018-02-14', '2018-02-15', '2018-02-16', '2018-02-17', '2018-02-18', '2018-02-19', '2018-02-20', '2018-02-21',
     '2018-02-22', '2018-02-23', '2018-02-24', '2018-02-25']
game = ['Blackjack_M',
        'BoomingTown',
        'CardLord',
        'CaribbeanPoker',
        'FishTycoon',
        'HappyCards',
        'Scratch',
        '10000000',
        '10000200']
name = ['三七二十一',
        '快乐大本营',
        '王牌',
        '加勒比扑克',
        '水产大亨',
        '乐三张',
        '吉星高照',
        '捕鱼',
        '中发白']

conn = connect(host='lg-15-163.ko.cn', port=21050)
cur = conn.cursor()

for i in t:
    print i
    print '======================================================'
    adate = i
    index = 0
    for j in game:
        print j,
        print name[index]
        index += 1
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        # 历史首次充值人数	历史首次充值用户充值金额
        sql = """select create_time_day,game_manu_id,count(distinct user_id) as num
        from stats_bean_consume_log_v1
        where game_manu_id='%s'
        and create_time_day>'%s'
        and user_id in (
          select distinct user_id
          from stats_bean_consume_log_v1
          where game_manu_id='%s'
          and create_time_day='%s'
        )
        group by create_time_day,game_manu_id""" % (j, adate, j, adate)

        cur.execute(sql)
        result = cur.fetchall()

        if result:
            df = pd.DataFrame(result)
            print df.sort_values(by=0)
        else:
            print result

cur.close()
conn.close()
