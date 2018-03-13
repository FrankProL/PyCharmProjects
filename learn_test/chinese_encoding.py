#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/2/18 23:12
# @Author  : Frank
# @Site    : 
# @File    : chinese_encoding.py
# @Software: PyCharm
"""
# pycharm 运行
# x=raw_input('请输入：')
# print x

# windows 命令行运行
# x=raw_input(u'请输入：'.encode('gbk'))
# print x
# f=open('1.txt','w')
# f.write(x)
# f.close()

import sys
print sys.stdin.encoding
print sys.stdout.encoding
"""根据当前系统的标准输入输出编码方式进行编码解码"""
x=raw_input(u'请输入'.encode(sys.stdout.encoding))
f=open('1.txt','w')
f.write(x.decode(sys.stdin.encoding).encode('utf-8'))
f.close()

# ----------------------------------------------------------------------------------------------------------
"""
    https://www.cnblogs.com/51kata/p/5339448.html
    字符串在Python内部的表示是unicode编码。在做编码转换时，通常需要以unicode作为中间编码，即先将其他编码的字符串解码（decode）成unicode，再从unicode编码（encode）成另一种编码。 
    unicode 和 其它的编码字符串在python 是完全不同的两种数据类型，unicode的字符串时unicode类型的， 其它的是str类型。
    decode的作用是将其他编码的字符串转换成unicode编码， 其参数就是字符串的当前编码格式。如str.decode('utf-8')，表示将utf-8编码的字符串转换成unicode编码。 
    encode的作用是将unicode编码转换成其他编码的字符串， 其参数就是希望转换后的编码格式。如str.encode('utf-8')，表示将unicode编码的字符串转换成utf-8编码。
"""
str = "中文"
print str
str = str.decode('utf-8').encode(sys.getfilesystemencoding())
print str
print sys.getfilesystemencoding()

# ----------------------------------------------------------------------------------------------------
'''
python 2.X版本的中文编码一直是一个头疼的事，这里主要解决中文列表或者字典的中文输出打印
'''
import json

dic = {"course": "我爱python"}
print dic
# 转化成json输出
print json.dumps(dic, encoding="utf-8", ensure_ascii=False)
# {"course": "我爱python"}

list = ["我", "python", "学习"]
print list
# 分别输出
for s in list:
    print s  # 分别为中文
# 通过转化json.dumps输出
print json.dumps(list, encoding="utf-8", ensure_ascii=False)
# ["我", "python", "学习"]

print '============================='

# 对于 obj = [u'\u7ef3\u5b50', u'\u5e26\u5b50'] 这种情况， 使用：print(repr(obj).decode('unicode-escape'))
print(repr(list).decode('unicode-escape'))
print(repr(dic).decode('unicode-escape'))

# 对于 obj = ['绳子','带子'] 这种情况，使用：print(repr(obj).decode('string-escape'))
print(repr(list).decode('string-escape'))
print(repr(dic).decode('string-escape'))