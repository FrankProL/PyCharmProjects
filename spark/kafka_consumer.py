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
"""
python读取kafka数据
https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html
"""

def writefile(L=[]):
    with open('ip.txt', 'w') as f:
        for s in L:
            f.write(s)
            f.write('\n')
        f.close()


datalist = []
iplist = []
i = 0
"""消费者(读取目前最早可读的消息)
    auto_offset_reset:重置偏移量，earliest移到最早的可用消息，latest最新的消息，默认为latest
    源码定义:{'smallest': 'earliest', 'largest': 'latest'}
"""
# consumer = KafkaConsumer('phone-game-userinfo',auto_offset_reset='earliest',bootstrap_servers=['172.23.11.150:9092'])
# for message in consumer:
#     print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
#                                           message.offset, message.key,
#                                           message.value))
#     i+=1
#     if i>100: break

"""消费者(手动设置偏移量)"""
# consumer = KafkaConsumer('phone-game-userinfo', bootstrap_servers=['172.23.11.150:9092'])
consumer = KafkaConsumer('phone-game-userlogin-kong', bootstrap_servers=['172.23.11.150:9092'])
print (consumer.partitions_for_topic("phone-game-userinfo"))  # 获取phone-game-userinfo主题的分区信息
print (consumer.topics())  # 获取主题列表
print (consumer.subscription())  # 获取当前消费者订阅的主题
print (consumer.assignment())  # 获取当前消费者topic、分区信息
print (consumer.beginning_offsets(consumer.assignment()))  # 获取当前消费者可消费的偏移量
# consumer.seek(TopicPartition(topic=u'phone-game-userinfo', partition=0), 100875)  # 重置偏移量，从第50个偏移量消费
consumer.seek(TopicPartition(topic=u'phone-game-userlogin-kong', partition=0), 100)
for message in consumer:
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value.decode('utf-8')))
    # print (message)
#     data = message.value[16:-1].split(',')
#     guid = data[0].split('=')[1]
#     ip = data[14].split('=')[1]
#     cTime = data[15].split('=')[1]
#     createTime = time.strftime('%Y-%m-%d', time.strptime(cTime, '%a %b %d %H:%M:%S CST %Y'))
#     userAccount = re.match(r"1\d{10}", data[21].split('=')[1], re.M | re.I)
#     if userAccount:
#         userAccount = userAccount.group()
#     # print (userAccount)
#     line = [guid, ip, createTime, userAccount]
#     datalist.append(line)
    i += 1
    if i > 100:
        break
# df = pd.DataFrame(datalist, index=None, columns=['guid', 'ip', 'createTime', 'userAccount'])
# # print df
#
# with open('ip_addr.txt','r') as ipaddr:
#     for line in ipaddr:
#         try:
#             a=json.loads(line)
#             ip_reg=[a[u'data'][u'ip'].strip('\r\n'),a[u'data'][u'region']]
#             iplist.append(ip_reg)
#         except:
#             pass
# df_ip=pd.DataFrame(iplist,columns=['ip','region'])
#
# df_result=pd.merge(df,df_ip,on='ip',suffixes=('','_r'),how='left')
# df_result.to_csv('user_data.csv',sep=',',encoding='utf-8',index=False)
# region_result=pd.DataFrame(df_result.groupby(['region'])['guid'].count().sort_values())
# region_result.to_excel('region.xlsx')

# writefile(df['ip'])
# toSave=df.groupby(['createTime'])['guid'].count()
# pd.DataFrame(toSave).to_excel('usernum_day.xlsx')


"""消费者(订阅多个主题)"""
# consumer = KafkaConsumer(bootstrap_servers=['172.23.11.150:9092'])
# consumer.subscribe(topics=('test', 'test0'))  # 订阅要消费的主题
# print (consumer.topics())
# print (consumer.position(TopicPartition(topic=u'test', partition=0)))  # 获取当前主题的最新偏移量
# for message in consumer:
#     print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
#                                           message.offset, message.key,
#                                           message.value))

"""消费者(手动拉取消息)   ?  """
# consumer = KafkaConsumer(bootstrap_servers=['172.23.11.150:9092'])
# # consumer.subscribe(topics=('test', 'test0'))
# consumer.subscribe(topics=('phone-game-userinfo'))
# consumer.topics()                                       # 必须先获取主题列表之后，才能重置偏移量
# consumer.seek(TopicPartition(topic=u'phone-game-userinfo', partition=0), 50)
# while True:
#     msg = consumer.poll(timeout_ms=5)  # 从kafka获取消息
#     print msg
#     time.sleep(1)
#     i+=1
#     if i>100:
#         break

"""消费者(消息挂起与恢复)"""
# from kafka import KafkaConsumer
# from kafka.structs import TopicPartition
# import time
#
# consumer = KafkaConsumer(bootstrap_servers=['172.21.10.136:9092'])
# consumer.subscribe(topics=('test'))
# consumer.topics()
# consumer.pause(TopicPartition(topic=u'test', partition=0))
# num = 0
# while True:
#     print num
#     print consumer.paused()   #获取当前挂起的消费者
#     msg = consumer.poll(timeout_ms=5)
#     print msg
#     time.sleep(2)
#     num = num + 1
#     if num == 10:
#         print "resume..."
#         consumer.resume(TopicPartition(topic=u'test', partition=0))
#         print "resume......"