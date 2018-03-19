#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/3/19 23:21
# @Author  : Frank
# @Site    : 
# @File    : requests_test.py
# @Software: PyCharm
"""
import requests

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
# response = requests.get('http://www.douban.com')
response = requests.get('http://www.douban.com',headers=header)  # 模拟浏览器访问，避免一些反爬虫
print response.text
# print response.content

# response = requests.get('http://www.haoyisheng.com')
# print response.text     # 中文出现乱码
# print response.content
