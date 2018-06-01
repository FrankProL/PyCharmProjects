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


def writefile(L=[]):
    with open('ip.txt', 'w') as f:
        for s in L:
            f.write(s)
            f.write('\n')
        f.close()


datalist = []
i = 0
"""消费者(读取目前最早可读的消息)
    auto_offset_reset:重置偏移量，earliest移到最早的可用消息，latest最新的消息，默认为latest
    源码定义:{'smallest': 'earliest', 'largest': 'latest'}
"""
# consumer = KafkaConsumer('phone-game-userlogin-kong',auto_offset_reset='earliest',bootstrap_servers=['172.23.11.150:9092'])
# for message in consumer:
#     print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
#                                           message.offset, message.key,
#                                           message.value.decode('utf-8')))
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
consumer.seek(TopicPartition(topic=u'phone-game-userlogin-kong', partition=0), 1)
print(consumer.end_offsets(consumer.assignment()))    # Get the last offset for the given partitions
print(consumer.end_offsets([TopicPartition(topic='phone-game-userlogin-kong', partition=0)])) # 同上一句等价
t= '2018-05-10'
timeArray =time.strptime(t,'%Y-%m-%d')
timeStamp=int(time.mktime(timeArray))
print(consumer.offsets_for_times({TopicPartition(topic='phone-game-userlogin-kong', partition=0):timeStamp}))
# for message in consumer:
#     # print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
#     #                                       message.offset, message.key,
#     #                                       message.value.decode('utf-8')))
#     # print (message.value.decode('utf-8'))
#     # print (message.offset)
#     data = message.value[17:].split(',')
#     guid = data[0].split(':')[1]
#     loginDate = data[3][10:]
#     loginDateFormat = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(loginDate, '%a %b %d %H:%M:%S CST %Y'))
#     loginDay = time.strftime('%Y-%m-%d', time.strptime(loginDate, '%a %b %d %H:%M:%S CST %Y'))
#     line = [guid, loginDateFormat,loginDay]
#     datalist.append(line)
#     i += 1
#     if i > 99:
#         break
# df = pd.DataFrame(datalist, index=None, columns=['guid', 'loginDateFormat','loginDay'])
# print df
# df.to_csv('login_data.csv',sep=',',encoding='utf-8',index=False)
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

consumer.close()