#!/usr/bin/python
# encoding: utf-8


"""
@author: 大圣
@contact: excelchart@sina.cn
@file: xinwenspider.py
@time: 2015/12/9 0009 上午 5:41
"""


import requests
from lxml import etree


def getNewsURLList(baseURL):
    x=requests.get(baseURL)
    html =  x.content.decode('gbk')

    selector = etree.HTML(html)

    contents = selector.xpath('//div[@id="content_right"]/div[@class="content_list"]/ul/li[div]')
    for eachlink in contents:
        url = eachlink.xpath('div/a/@href')[0]
        title = eachlink.xpath('div/a/text()')[0]
        ptime = eachlink.xpath('div[@class="dd_time"]/text()')[0]
        yield(title,url,ptime)

def getNewsContent(urllist):
    for title,url,ptime in urllist:
        x=requests.get(url)
        html = x.content.decode('gbk')
        selector = etree.HTML(html)
        contents=selector.xpath('//div[@class="left_zw"]/p/text()')
        news='\r\n'.join(contents)
        yield title,url,ptime,news

if __name__=='__main__':
    urltemplate = 'http://www.chinanews.com/scroll-news/mil/{0}/{1}{2}/news.shtml'

    testurl = urltemplate.format('2015','10','20')

    print testurl

    urllist = getNewsURLList(testurl)

    # for title,url,ptime in urllist:
    #     print title,url,ptime

    newscontens = getNewsContent(urllist)
    f=open('news.txt','w')
    w = lambda x: f.write((x+u'\r\n').encode('utf-8'))
    for title,url,ptime,news in newscontens:
        w (u'~'*100)
        w(title)
        w(url)
        w(ptime)
        w(news)
    f.close()

