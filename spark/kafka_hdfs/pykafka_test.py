#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/31 14:44
# @Author  : Frank
# @Site    : 
# @File    : pykafka_test.py
# @Software: PyCharm
"""

"""https://github.com/Parsely/pykafka
    https://www.jianshu.com/p/bfeceb3548ad
"""
import Queue

from pykafka import KafkaClient

client = KafkaClient(hosts='172.23.11.150:9092')
topic = client.topics['kzmg_hunter_login']
# consumer = topic.get_simple_consumer()
# for message in consumer:
#     if message is not None:
#         print (message.offset, message.partition)

balanced_consumer = topic.get_balanced_consumer(
    consumer_group='testgroup',
    auto_commit_enable=True,
    zookeeper_connect='172.23.11.150:2181'
)
for message in balanced_consumer:
    if message is not None:
        print (message.offset, message.partition)
