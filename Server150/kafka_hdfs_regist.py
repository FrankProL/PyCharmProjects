#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/12 16:11
# @Author  : Frank
# @Site    : 
# @File    : kafka_hdfs_regist.py
# @Software: PyCharm
"""
from kafka import KafkaConsumer, TopicPartition
from hdfs import InsecureClient
import ConfigParser
"""
注册数据
link @ kafka_hdfs_regist2.py
"""

def save_jsondata(client, consumer, filePath, append_sep):
    i = 0
    Tag = True
    while Tag:
        with client.write(filePath, encoding='utf-8', overwrite=False, append=True) as fs:
            for message in consumer:
                fs.write(message.value.decode('utf-8') + '\n')
                i += 1
                if i<2031000:
                    if i % (append_sep*1000) == 0:
                        print (i, message.offset, message.partition)
                        break
                else:
                    if i % append_sep == 0:
                        print (i, message.offset, message.partition)
                        break


if __name__ == '__main__':
    config = ConfigParser.RawConfigParser()
    config.read('kafka_to_hdfs_regist.cfg')

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
