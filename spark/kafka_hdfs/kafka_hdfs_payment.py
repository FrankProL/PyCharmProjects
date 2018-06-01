#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/28 17:18
# @Author  : Frank
# @Site    : 
# @File    : kafka_consumer.py
# @Software: PyCharm
"""
import time
import json
from kafka import KafkaConsumer, TopicPartition
from hdfs import InsecureClient

consumer = KafkaConsumer('kzmg_all_payment', bootstrap_servers=['172.23.11.150:9092'])
# print (consumer.partitions_for_topic("kzmg_all_payment"))  # 获取phone-game-userinfo主题的分区信息
print (consumer.topics())  # 获取主题列表
# print (consumer.subscription())  # 获取当前消费者订阅的主题
# print (consumer.assignment())  # 获取当前消费者topic、分区信息
# print (consumer.beginning_offsets(consumer.assignment()))  # 获取当前消费者可消费的偏移量
# print(consumer.end_offsets(consumer.assignment()))
consumer.seek(TopicPartition(topic=u'kzmg_all_payment', partition=0),125000)
num=consumer.end_offsets(consumer.assignment()).values()[0]
print(num)
i = 0
# t= '2018-05-22'
# timeArray =time.strptime(t,'%Y-%m-%d')
# timeStamp=int(time.mktime(timeArray))
# print(consumer.offsets_for_times({TopicPartition(topic='kzmg_all_payment', partition=0):timeStamp}))
client = InsecureClient('http://lg-11-152.ko.cn:50070', user='kzcq')
print (dir(client))
filePath = '/user/kzcq/datatest/kzmg_payment.json'
tag_list = []

# for message in consumer:
#     print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
#                                           message.offset, message.key,
#                                           message.value.decode('utf-8')))
#     print type(message.value)
#     i+=1
#     if i>10:
#         break
# for message in consumer:
#     client.write(filePath, message.value.decode('utf-8')+'\n',encoding='utf-8', overwrite=False, append=True)
#     if message.offset >= num - 1:
#         print('i   offset')
#         print (i)
#         print (message.offset)
#         break

with client.write(filePath, encoding='utf-8', overwrite=True) as fs:
    for message in consumer:
        fs.write(message.value.decode('utf-8')+'\n')
        # json.dump(message.value.decode('utf-8'),fs)

        i += 1
        if message.offset >= num-1:
            print('i   offset')
            print (i)
            print (message.offset)
            break
        if i%1000==0:
            print i
consumer.close()
