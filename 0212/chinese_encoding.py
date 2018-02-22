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
