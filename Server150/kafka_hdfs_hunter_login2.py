#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/31 10:29
# @Author  : Frank
# @Site    : 
# @File    : kafka_hdfs_hunter_login2.py
# @Software: PyCharm
"""
from kafka import KafkaConsumer
from hdfs import InsecureClient

"""kzmg_hunter_login 从最早的offset开始读取数据，保存到hdfs，300000条分割为一个文件"""


def save_jsondata(client, consumer):
    i = 0
    Tag = True
    while Tag:
        filePath = '/user/kzcq/data_in_json/kzmg_hunter_login/kzmg_hunter_login_%010d.json' % (i)
        with client.write(filePath, encoding='utf-8', overwrite=True) as fs:
            for message in consumer:
                fs.write(message.value.decode('utf-8') + '\n')
                i += 1
                if (i) % 300000 == 0:
                    break
                # if message.offset >= datanum - 1:
                #     print('i   offset')
                #     print (i)
                #     print (message.offset)
                #     Tag = False
                #     break
                if i % 10000 == 0:
                    print (i, message.offset, message.partition)


if __name__ == '__main__':
    topic = 'kzmg_hunter_login'
    client = InsecureClient('http://lg-11-152.ko.cn:50070', user='kzcq')

    consumer = KafkaConsumer('kzmg_hunter_login', bootstrap_servers=['172.23.11.150:9092'],
                             auto_offset_reset='earliest')
    consumer.topics()
    # consumer.seek(TopicPartition(topic, 0), 0)
    for key, value in consumer.end_offsets(consumer.assignment()).items():
        print (key, value)
    save_jsondata(client, consumer)
