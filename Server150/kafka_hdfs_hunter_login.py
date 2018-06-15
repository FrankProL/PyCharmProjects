#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/14 11:23
# @Author  : Frank
# @Site    : 
# @File    : kafka_hdfs_hunter_login.py
# @Software: PyCharm
"""
import json

from collections import defaultdict

from datetime import datetime
from kafka import KafkaConsumer, TopicPartition
from hdfs import InsecureClient
import ConfigParser

"""
登陆数据
"""


def save(client, filePath, tmpDict):
    for key, value in tmpDict.items():
        filePathNew = ''
        filePathNew = filePath + key + '.txt'
        with client.write(filePathNew, encoding='utf-8', overwrite=False, append=True) as fs:
            fs.write(''.join(value))
    tmpDict.clear()


def save_jsondata(client, consumer, filePath, append_sep):
    i = 0
    tmpDict = defaultdict(list)
    for message in consumer:
        data = json.loads(message.value, encoding='utf-8')
        loginDate = data.get(u'login_time', 'null')[0:10]

        tmpDict[loginDate].append(message.value.decode('utf-8') + '\n')

        # filePathNew = ''
        # filePathNew = filePath + loginDate + '.txt'
        # with client.write(filePathNew, encoding='utf-8', overwrite=False,append=True) as fs:
        #     fs.write(message.value.decode('utf-8') + '\n')
        i += 1
        if i < 13884839:
            if i % (append_sep * 10) == 0:
                save(client, filePath, tmpDict)
                print (i, message.offset, message.partition, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        else:
            if i % append_sep == 0:
                save(client, filePath, tmpDict)
                print (i, message.offset, message.partition, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


if __name__ == '__main__':
    config = ConfigParser.RawConfigParser()
    config.read('kafka_hdfs_hunter_login.cfg')

    filePath = config.get('Section1', 'filePath')
    topic = config.get('Section1', 'topic')
    append_sep = config.getint('Section1', 'append_sep')

    client = InsecureClient('http://lg-11-152.ko.cn:50070', user='kzcq')

    consumer = KafkaConsumer(topic, bootstrap_servers=['172.23.11.150:9092'])
    consumer.topics()
    print (consumer.subscription())
    print (consumer.assignment())
    print (consumer.beginning_offsets(consumer.assignment()))
    print(consumer.end_offsets(consumer.assignment()))
    for key, value in consumer.end_offsets(consumer.assignment()).items():
        print (key, value)
        consumer.seek(key, 0)
    save_jsondata(client, consumer, filePath, append_sep)
    consumer.close()
