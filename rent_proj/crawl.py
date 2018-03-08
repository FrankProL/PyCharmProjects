#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/3/7 18:42
# @Author  : Frank
# @Site    : 
# @File    : crawl.py
# @Software: PyCharm
"""
from bs4 import BeautifulSoup
from urlparse import urljoin
import requests
import csv

url = "http://bj.58.com/pinpaigongyu/pn/{page}/?minprice=2000_4000"

#已完成的页数序号，初时为0
page = 0

csv_file = open("rent.csv","wb")
csv_writer = csv.writer(csv_file, delimiter=',')

while True:
    page += 1
    print "fetch: ", url.format(page=page)
    response = requests.get(url.format(page=page))
    html = BeautifulSoup(response.text)
    house_list = html.select(".list > li")

    # 循环在读不到新的房源时结束
    if not house_list:
        break

    for house in house_list:
        house_title = house.select("h2")[0].string.encode("utf8")
        house_url = urljoin(url, house.select("a")[0]["href"])
        house_info_list = house_title.split()

        # 如果第二列是公寓名则取第一列作为地址
        if "公寓" in house_info_list[1] or "青年社区" in house_info_list[1]:
            house_location = house_info_list[0]
        else:
            house_location = house_info_list[1]

        house_money = house.select(".money")[0].select("b")[0].string.encode("utf8")
        csv_writer.writerow([house_title, house_location, house_money, house_url])

csv_file.close()

""" https://www.shiyanlou.com/courses/599/labs/1978/document
    高德API+Python解决租房问题
        python crawler.py                   获取租房信息 rent.csv      
        python -m SimpleHTTPServer 3000     打开服务器，浏览器访问localhost:3000查看效果       
"""

"""
#导入csv
import csv

# 打开rent.csv文件
csv_file = open("rent.csv","wb") 

# 创建writer对象，指定文件与分隔符
csv_writer = csv.writer(csv_file, delimiter=',')

# 写一行数据
csv_writer.writerow([house_title, house_location, house_money, house_url])

#关闭文件
csv_file.close()
"""

"""
requests是一个对使用者非常友好的http库

# 抓取目标页面
response = requests.get(url.format(page=page))

# 获取页面正文
response.text
"""

"""
Beautiful Soup是一个用来解析html或者xml文件的库，支持元素选择器，使用起来也非常方便：

# 创建一个BeautifulSoup对象
html = BeautifulSoup(response.text)

# 获取class=list的元素下的所有li元素
house_list = html.select(".list > li")

# 得到标签包裹着的文本
house.select("h2")[0].string.encode("utf8")

# 得到标签内属性的值
house.select("a")[0]["href"]

"""