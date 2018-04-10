#!/usr/bin/python
# encoding: utf-8


"""
@author: 大圣
@contact: excelchart@sina.cn
@file: 02.loadzip.py
@time: 2015/12/16 0016 下午 6:35
"""


import json
from pymongo import MongoClient

conn = MongoClient('localhost')
db = conn.beifeng
col = db.test.zips
col.remove(None)
f = open('zips.json')
for line in f:
    x=json.loads(line)
    #print x
    col.insert_one(x)
f.close()