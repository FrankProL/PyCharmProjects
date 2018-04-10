#!/usr/bin/python
# encoding: utf-8


"""
@author: 大圣
@contact: excelchart@sina.cn
@file: 04.spaggdemo.py
@time: 2015/12/16 0016 下午 9:19
"""


from pymongo import MongoClient
from pymongo.write_concern import WriteConcern
from faker import Factory
conn = MongoClient('localhost')
db = conn.beifeng
col = db.test.zips

#
count=col.count('state')
print count

# cursor= col.distinct('state')
#
# for doc in cursor:
#     print doc
# print cursor

# func = '''
#     function(cur,result){
#     result.count += 1
#     }
#     '''
# cursor = col.group(
#     {'state':1,'city':1},
#     {},
#     {'count':0},
#     func
# )

mapfunc = '''
   function(){
     emit({'state':this.state,'city':this.city},1);
   }
'''
redfunc = '''
   function(key,values){
      return values.length;
   }
'''

col.map_reduce(mapfunc,redfunc,query={},out='test.results')
# for doc in cursor:
#     print doc