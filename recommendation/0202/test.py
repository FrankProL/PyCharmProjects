#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/3/14 14:05
# @Author  : Frank
# @Site    : 
# @File    : onelinepy.py
# @Software: PyCharm
"""
import csv
from collections import defaultdict
from datetime import datetime

options = {
        'fieldnames': ('movieid', 'title', 'release', 'video', 'url'),
        'delimiter': '|',
        'restkey': 'genre'
    }
options.update()
print options

parse_int = lambda r, k: int(r[k])
parse_date = lambda r, k: datetime.strptime(r[k], '%d-%b-%Y') if r[k] else None
with open('u.item', 'rb') as movies:
    reader = csv.DictReader(movies, **options)

    # column=[row['release'] for row in reader]
    # print column
    t=0
    for row in reader:                                  # 文件读取一次，当reader遍历一次之后，就指向空了
        print (type(row))
        print (row)
        row['movieid'] = parse_int(row, 'movieid')
        print (row['movieid'])
        row['release'] = parse_date(row, 'release')
        print (row['release'])
        print (row['video'])
        if t<10:
            break

# from rec_movies import load_reviews
# reviews = defaultdict(dict)
# i=0
# for review in load_reviews('u.data'):
#     print review
#     i+=1
#     reviews[review['userid']][review['movieid']] = review
#     if i>10:
#         print reviews
#         break

# {196: {242: {'movieid': 242, 'userid': 196, 'timestamp': datetime.datetime(1997, 12, 4, 23, 55, 49), 'rating': 3}}}