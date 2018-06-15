#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/28 17:18
# @Author  : Frank
# @Site    : 
# @File    : kafka_hdfs_hunter_login_thread.py
# @Software: PyCharm
"""
"""
每个分区启动一个consumer线程，offset重置为0，由于seek API，导致kafka有新数据进来时，offset自动变为最新值
"""
import thread
from kafka import KafkaConsumer, TopicPartition
from hdfs import InsecureClient

locks=[]
def save_jsondata(client, consumer, datanum, name_mid_num,lock):
    tmpOffset = 0
    i = 0
    Tag = True
    while Tag:
        filePath = '/user/kzcq/data_in_json/kzmg_hunter_login/kzmg_hunter_login_%s_%010d.json' % (name_mid_num, tmpOffset)
        with client.write(filePath, encoding='utf-8', overwrite=True) as fs:
            for message in consumer:
                fs.write(message.value.decode('utf-8') + '\n')
                if (message.offset + 1) % 300000 == 0:
                    tmpOffset = message.offset + 1
                    break
                i += 1
                if message.offset >= datanum - 1:
                    print('i   offset')
                    print (i)
                    print (message.offset)
                    Tag = False
                    break
                if i % 1000 == 0:
                    print (i,message.offset,message.partition)
    consumer.close()
    lock.release()


if __name__ == '__main__':
    client = InsecureClient('http://lg-11-152.ko.cn:50070', user='kzcq')

    consumer = KafkaConsumer('kzmg_hunter_login', bootstrap_servers=['172.23.11.150:9092'])
    consumer.topics()
    for key, value in consumer.end_offsets(consumer.assignment()).items():
        print (key, value)
        name_mid_num = str(key)[53:54]
        # name_mid_num=str(key)[51:52]
        print(name_mid_num)

        locals()['consumer' + name_mid_num]=KafkaConsumer('kzmg_hunter_login', bootstrap_servers=['172.23.11.150:9092'])
        locals()['consumer' + name_mid_num].topics()
        locals()['consumer' + name_mid_num].seek(key, 0)
        datanum = value
        try:
            lock = thread.allocate_lock()
            lock.acquire()
            locks.append(lock)
            thread.start_new_thread(save_jsondata, (client, locals()['consumer'+name_mid_num], datanum, name_mid_num,lock))
        except:
            print ('error: unable to start thread')
    consumer.close()
    for i in locks:
        while i.locked():
            pass