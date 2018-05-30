#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/2 17:18
# @Author  : Frank
# @Site    : 
# @File    : kafka_consumer.py
# @Software: PyCharm
"""
import re
import time
import pandas as pd
import json
from kafka import KafkaConsumer, TopicPartition
from hdfs import InsecureClient

consumer = KafkaConsumer('kzmg_hunter_login', bootstrap_servers=['172.23.11.150:9092'])
print (consumer.partitions_for_topic("kzmg_hunter_login"))  # 获取phone-game-userinfo主题的分区信息
print (consumer.topics())  # 获取主题列表
print (consumer.subscription())  # 获取当前消费者订阅的主题
print (consumer.assignment())  # 获取当前消费者topic、分区信息
print (consumer.beginning_offsets(consumer.assignment()))  # 获取当前消费者可消费的偏移量
print(consumer.end_offsets(consumer.assignment()))
consumer.seek(TopicPartition(topic=u'kzmg_hunter_login', partition=0), 10)
i = 0
# t= '2018-05-22'
# timeArray =time.strptime(t,'%Y-%m-%d')
# timeStamp=int(time.mktime(timeArray))
# print(consumer.offsets_for_times({TopicPartition(topic='kzmg_hunter_login', partition=0):timeStamp}))
client = InsecureClient('http://lg-11-152.ko.cn:50070', user='kzcq')
print (dir(client))
filePath = '/user/kzcq/datatest/kzmg_login1.json'
tag_list = ['游戏ID',
            '区位标识',
            '账号ID',
            '游戏产品名称',
            '游戏语言',
            '游戏版本',
            '服务器标识',
            '登录设备',
            '设备序列号',
            '安卓ID',
            '设备分辨率',
            '设备OS',
            'OS版本',
            '注册登入（出）时间',
            '动作',
            '当前虚拟币余额',
            '登录IP',
            '角色等级',
            '角色声望',
            '动作属性',
            'OpenUDID',
            '角色名称',
            '用户帐号',
            '登录渠道',
            '角色ID']
with client.write(filePath, encoding='utf-8', overwrite=True) as fs:
    for message in consumer:
        # print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
        #                                       message.offset, message.key,
        #                                       message.value.decode('utf-8')))
        # print (message.value)

        # fs.write(message.value.decode('utf-8')+'\n')
        # json.dump(message.value.decode('utf-8'),fs)
        value=json.loads(message.value)
        line = value['message'].split('|')
        dic=dict(zip(tag_list,line))
        dic['timestamp']=value['@timestamp'][:10]
        # print (repr(dic).decode('string-escape'))
        fs.write(json.dumps(dic)+'\n')
        i += 1
        if i > 12345:
            break
        if i%1000==0:
            print i
consumer.close()
