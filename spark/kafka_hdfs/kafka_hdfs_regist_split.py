#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/28 17:18
# @Author  : Frank
# @Site    : 
# @File    : kafka_hdfs_regist_split.py
# @Software: PyCharm
"""
from kafka import KafkaConsumer, TopicPartition
from hdfs import InsecureClient


def save_jsondata(client, consumer, num, mid_name):
    tmpOffset = 0
    i = 0
    Tag = True
    while Tag:
        filePath = '/user/kzcq/datatest/kzmg_regist_%s_%010d.json' % (mid_name, tmpOffset)
        with client.write(filePath, encoding='utf-8', overwrite=True) as fs:
            for message in consumer:
                fs.write(message.value.decode('utf-8') + '\n')
                if (message.offset + 1) % 200000 == 0:
                    tmpOffset = message.offset + 1
                    break
                i += 1
                if message.offset >= num - 1:
                    print('i   offset')
                    print (i)
                    print (message.offset)
                    Tag = False
                    break
                if i % 1000 == 0:
                    print (i)


if __name__ == '__main__':
    client = InsecureClient('http://lg-11-152.ko.cn:50070', user='kzcq')

    consumer = KafkaConsumer('kzmg_all_regist', bootstrap_servers=['172.23.11.150:9092'])
    consumer.topics()
    for key, value in consumer.end_offsets(consumer.assignment()).items():
        print key, value
        consumer.seek(key, 0)
        num = value
        mid_name = str(key)[41:52]
        save_jsondata(client, consumer, num, mid_name)
    consumer.close()