#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/4/27 11:08
# @Author  : Frank
# @Site    : 
# @File    : json_test.py
# @Software: PyCharm
"""
"""
json.dumps	将 Python 对象编码成 JSON 字符串
json.loads	将已编码的 JSON 字符串解码为 Python 对象
    用于序列化的两个模块：
        json: 用于字符串和python数据类型间进行转换 
        pickle： 用于python特有的类型和python的数据类型间进行转换
    Json模块提供了四个功能：dumps、dump、loads、load
    pickle模块提供了四个功能：dumps、dump、loads、load
    json dumps把数据类型转换成字符串 dump把数据类型转换成字符串并存储在文件中  
    loads把字符串转换成数据类型  load把文件打开从字符串转换成数据类型
"""
import json

data=[{"ts": "2018-04-23 00:15:00", "user_online": 1, "guest_online": 0},
       {"ts": "2018-04-23 00:45:00", "user_online": 0, "guest_online": 0},
       {"ts": "2018-04-23 01:15:00", "user_online": 0, "guest_online": 0},
       {"ts": "2018-04-23 01:45:00", "user_online": 0, "guest_online": 0},
       {"ts": "2018-04-23 02:15:00", "user_online": 0, "guest_online": 0},
       {"ts": "2018-04-23 02:45:00", "user_online": 0, "guest_online": 0},
       {"ts": "2018-04-23 03:15:00", "user_online": 0, "guest_online": 0},
       {"ts": "2018-04-23 03:45:00", "user_online": 1, "guest_online": 0},
       {"ts": "2018-04-23 04:15:00", "user_online": 0, "guest_online": 0},
       {"ts": "2018-04-23 04:45:00", "user_online": 0, "guest_online": 0},
       {"ts": "2018-04-23 05:15:00", "user_online": 0, "guest_online": 0},
       {"ts": "2018-04-23 05:45:00", "user_online": 0, "guest_online": 0},
       {"ts": "2018-04-23 06:15:00", "user_online": 0, "guest_online": 0},
       {"ts": "2018-04-23 06:45:00", "user_online": 1, "guest_online": 0},
       {"ts": "2018-04-23 07:15:00", "user_online": 0, "guest_online": 0},
       {"ts": "2018-04-23 07:45:00", "user_online": 1, "guest_online": 0},
       {"ts": "2018-04-23 08:15:00", "user_online": 0, "guest_online": 0},
       {"ts": "2018-04-23 08:45:00", "user_online": 3, "guest_online": 0},
       {"ts": "2018-04-23 09:15:00", "user_online": 3, "guest_online": 0},
       {"ts": "2018-04-23 09:45:00", "user_online": 2, "guest_online": 0},
       {"ts": "2018-04-23 10:15:00", "user_online": 4, "guest_online": 0},
       {"ts": "2018-04-23 10:45:00", "user_online": 2, "guest_online": 0},
       {"ts": "2018-04-23 11:15:00", "user_online": 3, "guest_online": 0},
       {"ts": "2018-04-23 11:45:00", "user_online": 6, "guest_online": 0},
       {"ts": "2018-04-23 12:15:00", "user_online": 5, "guest_online": 0},
       {"ts": "2018-04-23 12:45:00", "user_online": 5, "guest_online": 0},
       {"ts": "2018-04-23 13:15:00", "user_online": 6, "guest_online": 0},
       {"ts": "2018-04-23 13:45:00", "user_online": 7, "guest_online": 0},
       {"ts": "2018-04-23 14:15:00", "user_online": 10, "guest_online": 0},
       {"ts": "2018-04-23 14:45:00", "user_online": 10, "guest_online": 0},
       {"ts": "2018-04-23 15:15:00", "user_online": 10, "guest_online": 0},
       {"ts": "2018-04-23 15:45:00", "user_online": 13, "guest_online": 0},
       {"ts": "2018-04-23 16:15:00", "user_online": 9, "guest_online": 0},
       {"ts": "2018-04-23 16:45:00", "user_online": 13, "guest_online": 0},
       {"ts": "2018-04-23 17:15:00", "user_online": 17, "guest_online": 0},
       {"ts": "2018-04-23 17:45:00", "user_online": 13, "guest_online": 0},
       {"ts": "2018-04-23 18:15:00", "user_online": 20, "guest_online": 0},
       {"ts": "2018-04-23 18:45:00", "user_online": 79, "guest_online": 0},
       {"ts": "2018-04-23 19:15:00", "user_online": 404, "guest_online": 0},
       {"ts": "2018-04-23 19:45:00", "user_online": 482, "guest_online": 0},
       {"ts": "2018-04-23 20:15:00", "user_online": 501, "guest_online": 0},
       {"ts": "2018-04-23 20:45:00", "user_online": 512, "guest_online": 0},
       {"ts": "2018-04-23 21:15:00", "user_online": 464, "guest_online": 0},
       {"ts": "2018-04-23 21:45:00", "user_online": 388, "guest_online": 0},
       {"ts": "2018-04-23 22:15:00", "user_online": 168, "guest_online": 0},
       {"ts": "2018-04-23 22:45:00", "user_online": 57, "guest_online": 0},
       {"ts": "2018-04-23 23:15:00", "user_online": 33, "guest_online": 0},
       {"ts": "2018-04-23 23:45:00", "user_online": 24, "guest_online": 0}]
import pandas as pd

df =pd.DataFrame(data)
print (df['user_online'].max())
