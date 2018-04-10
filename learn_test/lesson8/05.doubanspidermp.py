#!/usr/bin/python
# encoding: utf-8


"""
@author: 大圣
@contact: excelchart@sina.cn
@file: doubanjson.py
@time: 2015/12/9 0009 下午 9:08
"""
# http://www.douban.com/tag/小说/?focus=book
# http://www.douban.com/j/tag/items?start=0&limit=600&topic_id=255&topic_name=小说&mod=book


import requests
from lxml import etree
import time
import pymongo
from pymongo import MongoClient
from multiprocessing import Process,Queue

class DoubanSpider(object):
    @staticmethod
    def getBooksNumber():
        x =requests.get(u'http://www.douban.com/j/tag/items?start=0&limit=1&topic_id=255&topic_name=小说&mod=book'.encode('utf-8'))
        bookjson = x.json()
        booksnum = bookjson['total']
        return booksnum

    @staticmethod
    def getURLList(nPerRequest=10):
        dynurl = u'http://www.douban.com/j/tag/items?start={0}&limit={1}&topic_id=255&topic_name=小说&mod=book'
        booksnum=DoubanSpider.getBooksNumber()
        start = 0
        while start < booksnum:
            url = dynurl.format(start,nPerRequest).encode('utf-8')
            yield url
            start += nPerRequest

    @staticmethod
    def getOneBooksList(url):
        x = requests.get(url)
        bookjson= x.json()
        bookslist=bookjson['html']
        bookshtml = u'<dbook>'.encode('utf-8')+ bookslist + u'</dbook>'.encode('utf-8')
        doc = etree.fromstring(bookshtml)
        for eachbook in doc.xpath('//dl/dd'):
            bookname = eachbook.xpath('a/text()')[0]
            bookurl = eachbook.xpath('a/@href')[0]
            pubs = eachbook.xpath('div[@class="desc"]/text()')
            pub = pubs[0] if pubs else None
            rates = eachbook.xpath('div[@class="rating"]/span[@class="rating_nums"]/text()')
            rate = rates[0] if rates else None
            yield bookname,bookurl,pub,rate



class DoubanURLProducer(Process):
    def __init__(self,q):
        Process.__init__(self)
        self._q=q

    def run(self):
        for url in DoubanSpider.getURLList():
            self._q.put(url)
        self._q.put(None)





class DoubanMongoConsumer(Process):
    def __init__(self,q):
        Process.__init__(self)
        self._q=q
    def saveBook(self,url):
        conn = MongoClient('localhost')
        db = conn.beifeng
        doubanbooks = db.test.doubanbooks
        label = ['name','url','pub','rate']
        books = []
        for value in DoubanSpider.getOneBooksList(url):
            book=dict(zip(label,value))
            books.append(book)
        doubanbooks.insert_many(books,ordered=False)
        conn.close()

    def run(self):
        url = None
        while True:
            try :
                url = self._q.get()
            except:
                time.sleep(1)
                continue
            if url:
                self.saveBook(url)
            else :
                break




if __name__=='__main__':
   # for i,value in enumerate(DoubanSpider.getURLList()):
   #     print value
   #     for data in DoubanSpider.getOneBooksList(value):
   #         print data
   #     break
   # a=DoubanMongoConsumer(None)
   # a.saveBook('http://www.douban.com/j/tag/items?start=0&limit=10&topic_id=255&topic_name=小说&mod=book')
   q = Queue()
   producer=DoubanURLProducer(q)
   consumers=[DoubanMongoConsumer(q) for i in range(4)]
   producer.start()
   for c in consumers:
       c.start()

   for c in consumers:
       c.join()


