#!/usr/bin/python
# encoding: utf-8


"""
@author: 大圣
@contact: excelchart@sina.cn
@file: 04.bajiespider.py
@time: 2015/12/10 0010 下午 10:43
"""


#!/usr/bin/python
# encoding: utf-8


"""
@author: 大圣
@contact: excelchart@sina.cn
@file: baisejie.py
@time: 2015/12/9 0009 上午 8:33
"""


import requests
from lxml import etree


def getJokeList(baseurl='http://www.budejie.com/text/{0}'):
    nextPage = True
    pagenum = 1
    while nextPage:
        url=baseurl.format(pagenum)
        response = requests.get(url)
        selector=etree.HTML(response.text)

        jokes = selector.xpath('//div[@class="j-r-list-c-desc"]/text()')
        for joke in jokes:
            print joke
            yield joke

        hasNext= selector.xpath('//a[@class="pagenxt"]')
        if hasNext:
            pagenum += 1
        else :
            nextPage = False


if __name__=='__main__':
    f=open('basejie.txt','w')
    for joke in getJokeList():
        f.writelines(joke.encode('utf8'))
        f.writelines('\r\n')
        f.writelines('~'*100)
    f.close()
