#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/28 17:18
# @Author  : Frank
# @Site    : 
# @File    : kafka_hdfs_regist2.py
# @Software: PyCharm
"""
from kafka import KafkaConsumer, TopicPartition
from hdfs import InsecureClient

consumer = KafkaConsumer('kzmg_all_regist', bootstrap_servers=['172.23.11.150:9092'])
print (consumer.topics())  # 获取主题列表
consumer.seek(TopicPartition(topic=u'kzmg_all_regist', partition=0), 452920)
num=consumer.end_offsets(consumer.assignment()).values()[0]
print(num)
i = 0
client = InsecureClient('http://lg-11-152.ko.cn:50070', user='kzcq')

tmpOffset=0

Tag=True
while Tag:
    filePath = '/user/kzcq/datatest/kzmg_regist_%010d.json' % (tmpOffset)
    with client.write(filePath, encoding='utf-8', overwrite=True) as fs:
        for message in consumer:
            fs.write(message.value.decode('utf-8') + '\n')
            if (message.offset+1)%20000==0:
                tmpOffset=message.offset+1
                break
            i += 1
            if message.offset >= 452936 - 1:
                print('i   offset')
                print (i)
                print (message.offset)
                Tag = False
                break
            if i % 1000 == 0:
                print (i)
consumer.close()
