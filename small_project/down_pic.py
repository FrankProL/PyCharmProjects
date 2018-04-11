#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/4/11 10:21
# @Author  : Frank
# @Site    : 
# @File    : down_pic.py
# @Software: PyCharm
"""

# import urllib
# import urllib.request
import requests
import re

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}


def download_page(url):
    # response = urllib.request.urlopen(url)
    # data = response.read()
    # data = data.decode('GBK')
    # return data
    response = requests.get(url,proxies={'https':'socks5://127.0.0.1:1080'},headers=header)     # 加了代理和浏览器头，依然无法获取到正常的页面
    data=response.content.decode('utf-8')
    print data
    return data


def get_image(html):
    reg = r'src="(http.+?\.jpg)"'
    pattern = re.compile(reg)
    get_img = re.findall(pattern, html)
    num = 0
    for img in get_img:
        # urllib.request.urlretrieve(img, 'D:\picture\%s.jpg' % num)
        print img
        with open('%s.jpg'%num) as f:
            f.write(requests.get(img).content)
        num += 1
        print('正在下载第%s张照片' % num)
    return get_img

html = download_page("http://www.metarthunter.com/most-viewed/")
get_image(html)