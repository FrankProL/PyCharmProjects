#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/21 16:11
# @Author  : Frank
# @Site    : 
# @File    : hdfsFile.py
# @Software: PyCharm
"""
from hdfs.client import Client
from hdfs import InsecureClient
import pandas as pd


# with client.read(filePath) as fs:
# content=pd.read_parquet(fs,engine='fastparquet')
# content=pd.read_parquet('example_pa.parquet', engine='pyarrow')
# print(content)
# with client.write(filePath) as fs:
#     fs.write(js)

# 读取hdfs文件内容,将每行存入数组返回
def read_hdfs_file(client, filename):
    # with client.read('samples.csv', encoding='utf-8', delimiter='\n') as reader:
    #  for line in reader:
    # pass
    lines = []
    with client.read(filename, encoding='utf-8', delimiter='\n') as reader:
        for line in reader:
            # pass
            # print line.strip()
            lines.append(line.strip())
    return lines


# 创建目录
def mkdirs(client, hdfs_path):
    client.makedirs(hdfs_path)


# 删除hdfs文件
def delete_hdfs_file(client, hdfs_path):
    client.delete(hdfs_path)


# 上传文件到hdfs
def put_to_hdfs(client, local_path, hdfs_path):
    client.upload(hdfs_path, local_path, cleanup=True)


# 从hdfs获取文件到本地
def get_from_hdfs(client, hdfs_path, local_path):
    client.download(hdfs_path, local_path, overwrite=False)


# 追加数据到hdfs文件
def append_to_hdfs(client, hdfs_path, data):
    client.write(hdfs_path, data, overwrite=False, append=True)


# 覆盖数据写到hdfs文件
def write_to_hdfs(client, hdfs_path, data):
    client.write(hdfs_path, data, overwrite=True, append=False)


# 移动或者修改文件
def move_or_rename(client, hdfs_src_path, hdfs_dst_path):
    client.rename(hdfs_src_path, hdfs_dst_path)


# 返回目录下的文件
def list(client, hdfs_path):
    return client.list(hdfs_path, status=False)


if __name__ == '__main__':
    # client = Client('http://lg-11-152.ko.cn:50070')
    client = InsecureClient('http://lg-11-152.ko.cn:50070', user='kzcq')
    # mkdirs(client,'/user/kzcq/data_in_json/kzmg_all_payment')
    # mkdirs(client, '/user/kzcq/data_in_json/kzmg_all_regist')
    # mkdirs(client, '/user/kzcq/data_in_json/kzmg_hunter_login')
    # delete_hdfs_file(client,'/user/kzcq/datatest/kzmg_login.json')
    # delete_hdfs_file(client, '/user/kzcq/datatest/kzmg_login1.json')
    # delete_hdfs_file(client, '/user/kzcq/datatest/kzmg_payment.json')
    # delete_hdfs_file(client,'/user/kzcq/datatest/')
    # client.delete('/user/kzcq/data_in_json/kzmg_hunter_login',recursive=True)
    # client.makedirs('/user/kzcq/data_in_json/kzmg_hunter_login2/')
    # client.delete('/user/kzcq/datalogintest2/',recursive=True)
    # client.delete('/user/kzcq/datalogintest3',recursive=True)
    # client.makedirs('/user/kzcq/input/kzmg/logs/')

    data = {"sourceId": "null", "gid": "168", "unionid": "null", "otherId": "null", "deviceOs": "7.1.2",
            "ip": "182.18.63.162", "usrid": "10111", "isSynchronization": "1",
            "deviceSn": "CDF9D5C5-859F-4B39-83DA-0C810FE40DD7", "bindingTime": "2017-12-08 02:35:39",
            "openudid": "null", "adudid": "null", "otherUid": "null", "lastLoginTime": "2015-07-16 16:42:23",
            "createTime": "2015-07-16 16:42:23", "newUnionid": "null", "appudid": "null",
            "userAccount": "mahui_08@163.com", "guid": "40095", "deviceMac": "020000000000", "state": "2",
            "otherSourceId": "null"}
    client.write('/user/kzcq/input/kzmg/logs/test.txt', data, overwrite=True, append=False)
    append_to_hdfs(client,'/user/kzcq/input/kzmg/logs/test.txt',data)

    # client = InsecureClient('http://lg-15-79.ko.cn:50070', user='none_pass')
    # client.write('/user/tmp/test.txt', data, overwrite=True, append=False)
    # append_to_hdfs(client, '/user/tmp/test.txt', data)