#!/usr/bin/python
# encoding: utf-8


"""
@author: 大圣
@contact: excelchart@sina.cn
@file: 01mongodemo.py
@time: 2015/12/14 0014 下午 10:31
"""

import pymongo
from pymongo import MongoClient

conn = MongoClient('localhost')
db = conn.beifeng
students = db.test.students

#  设置写安全级别
# from pymongo.write_concern import WriteConcern
# students  = col.with_options(write_concern=WriteConcern(w=1,j=True))

students.remove(None)

#  嵌套文档
dasheng = {'name':'dasheng' ,
           'age' :30 ,
           'sex' :'m' ,
           'contact': {
               'email1' : 'abc@def.com' ,
               'email2' :'def@abc.net'
            }
           }

bajie = {'name':'bajie',
         'habit':{
             'habit1' : 'eat',
             'habit2' : 'sleep'
         }
         }

#1、插入记录
students.insert_one(dasheng)

x=students.insert_one(bajie)

# 2、批量插入
from faker import Factory
import random
def getFakeData(n=10):
    userfaker = Factory.create()
    label = ['name','address','email','age']
    result = []
    for i in range(n):
        x = [userfaker.name(),userfaker.address(),userfaker.email(),random.randint(10,40)]
        result.append(dict(zip(label,x)))
    return result

userinfo = getFakeData()
z=students.insert_many(userinfo,ordered=False)

# students.insert_one({'name':'haha'})
#
#
# #2、查询
import json
from bson import json_util

# cursor=students.find({})
# cursor=students.find({'name':'dasheng'})
# cursor=students.find({'name':{'$in':['dasheng','bajie']}})
#  年龄大于25岁
# cursor=students.find({'age':{'$gt':25}})
#  and
# cursor=students.find( { 'name':{'$in':['dasheng','bajie']},
#                         'age':{'$gt':25}
#                         }
#                       )
#   or
# cursor=students.find( {'$or':[ {'name':{'$in':['dasheng','bajie']}},
#                                {'age': {'$gt':30}}
#                                ]
#                        }
#                       )
#
# cursor = students.find( {'habit.habit2':'eat'})
# for student in cursor:
#     # print student
#     print json.dumps(student,indent=4,default=json_util.default)



#3.更新

# $inc , 如果记录中没有这个字段，会增加此字段

# students.update_many(
#     {},
#     {'$inc':
#          {'age':2}
#      }
# )

# $min
# students.update_many(
#     {'name':
#          {'$in':['dasheng','bajie']}
#      } ,
#     {'$min':
#          {'age':20}
#      }
# )
# $currentDate
# students.update_many(
#     {'name':
#          {'$in':['dasheng','bajie']}
#      } ,
#     { '$currentDate' :
#           {'create_time':True,
#            'mod_time':{'$type':'timestamp'}
#            }
#      }
# )

# # 更新整个内嵌文档
# students.update_one(
#     {'name':'dasheng'},
#     {'$set' :
#          {
#              'contact':{
#                  'email1':'beijing',
#                  'email2':'haidian'
#              }
#          }
#     }
# )
# # 更新内嵌文档部分字段
# students.update_one(
#     {'name':'dasheng'},
#     {'$set' : {
#         'contact.email1':'abcd@efg.com'
#     }}
# )

# 删除
students.remove({'name':'dasheng'})


# find and update

record=students.find_one_and_update(
    {},
    {'$set':{'locked':1},
     '$inc':{'age':2}
     },
    projection={'age':True,'name':True},
    sort =[('age',pymongo.DESCENDING)],
    return_document=pymongo.ReturnDocument.BEFORE
)