#!/usr/bin/python
# encoding: utf-8


"""
@author: 大圣
@contact: excelchart@sina.cn
@file: 03.aggdemo.py
@time: 2015/12/16 0016 下午 8:42
"""

from pymongo import MongoClient
from pymongo.write_concern import WriteConcern
from faker import Factory
conn = MongoClient('localhost')
db = conn.beifeng
col = db.test.zips
# 排序
# cursor = col.aggregate([
#     {'$sort':{'city':1,'state':1}},
#     {'$project':{
#         '_id':0,
#         'state':1,
#         'city':1,
#         'pop':1
#     }}
# ])
# 人口数量超过1000万的州
# cursor = col.aggregate([
#     { '$group': {'_id':'$state','totalPop' : {'$sum':'$pop'}}},
#     { '$match':{ 'totalPop': {'$gte': 10*1000*1000}}}
# ]
#
# )

# 每个州的平均城市人口
# cursor = col.aggregate([
#     { '$group':{'_id':{'state':'$state','city':'$city'},'pop': {'$sum':'$pop'}}},
#     { '$group':{'_id':'$_id.state','avgCityPop':{'$avg':'$pop'}}},
#     {'$sort':{'avgCityPop':-1}}
# ]
# )

# 每个州人口最多和最少的城市
cursor = col.aggregate([
    { '$group':{'_id':{'state':'$state','city':'$city'},'pop':{'$sum':'$pop'}}},
    {'$sort' : {'pop':1}},
    { '$group':{'_id':'$_id.state',
                'biggestCity':{'$last':'$_id.city'},
                'biggestPop':{'$last':'$pop'},
                'smallestCity':{'$first':'$_id.city'},
                'smallestPop' : {'$first':'$pop'}
                }
      },
    {'$project':{
        '_id':0,
        'biggestCity':{'city':'$biggestCity','pop':'$biggestPop'},
        'smallestCity':{'city':'$smallestCity','pop':'$smallestPop'}
    }}

])


for doc in cursor:
    print doc