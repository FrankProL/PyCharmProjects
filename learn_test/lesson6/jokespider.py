#!/usr/bin/python
# encoding: utf-8


"""
@author: 大圣
@contact: excelchart@sina.cn
@file: jokespider.py
@time: 2015/12/14 0014 下午 5:43
"""
import requests
from lxml import etree
from jokemodel import Joke,session
def getJokeList(baseurl='http://www.budejie.com/text/{0}'):
    nextPage = True
    pagenum = 1
    while nextPage:
        url=baseurl.format(pagenum)
        response = requests.get(url)
        selector=etree.HTML(response.text)

        jokes = selector.xpath('//div[@class="j-r-list-c-desc"]/text()')
        for joke in jokes:
            yield joke

        hasNext= selector.xpath('//a[@class="pagenxt"]')
        if hasNext:
            pagenum += 1
        else :
            nextPage = False


if __name__=='__main__':
    for i,joke in enumerate(getJokeList()):
        session.add(Joke(content =joke.encode('utf8')))
        if (i%10==0):
            session.commit()
    session.commit()