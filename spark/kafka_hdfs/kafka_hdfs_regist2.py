#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/12 16:11
# @Author  : Frank
# @Site    : 
# @File    : kafka_hdfs_regist2.py
# @Software: PyCharm
"""
from kafka import KafkaConsumer, TopicPartition
from hdfs import InsecureClient


def save_jsondata(client, consumer, filePath,i):
    for message in consumer:
        with client.write(filePath,encoding='utf-8',overwrite=False,append=True) as fs:
            fs.write(message.value.decode('utf-8')+'\n')
        i += 1
        if message.offset%1000==0:
            print('i   offset')
            print (i)
            print (message.offset,message.partition)
        if message.offset>522200:
            print('i   offset')
            print (i)
            print (message.offset, message.partition)

def save_jsondata2(client, consumer,filePath ,i):
    i = 0
    Tag = True
    while Tag:
        with client.write(filePath, encoding='utf-8', overwrite=False,append=True) as fs:
            for message in consumer:
                fs.write(message.value.decode('utf-8') + '\n')
                i += 1
                if (i) % 1000 == 0:
                    print (i, message.offset, message.partition)
                    break


if __name__ == '__main__':
    filePath='/user/kzcq/input/kzmg/logs/kzmg_all_regist.txt'

    client = InsecureClient('http://lg-11-152.ko.cn:50070', user='kzcq')

    consumer = KafkaConsumer('kzmg_all_regist', bootstrap_servers=['172.23.11.150:9092'])
    consumer.topics()
    print (consumer.subscription())  # 获取当前消费者订阅的主题
    print (consumer.assignment())  # 获取当前消费者topic、分区信息
    print (consumer.beginning_offsets(consumer.assignment()))  # 获取当前消费者可消费的偏移量
    print(consumer.end_offsets(consumer.assignment()))
    for key, value in consumer.end_offsets(consumer.assignment()).items():
        print key, value
        consumer.seek(key, 0)
    i=0
    save_jsondata2(client, consumer,filePath,i)
    consumer.close()