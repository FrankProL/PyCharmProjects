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

"""使用python通过hdfs client读取hdfs文件 https://hdfscli.readthedocs.io/en/latest/quickstart.html
https://hdfscli.readthedocs.io/en/latest/quickstart.html#instantiating-a-client
    通过pandas的read_parquet读取parquet文件，pandas 0.21 introduces new functions for Parquet:
https://pandas.pydata.org/pandas-docs/version/0.21/io.html#io-parquet
    需要使用pyarrow或fastparquet模块辅助，但都没安装成功，pyarrow提示和ipaddress模块冲突，fastparquet下载太慢、下载不下来
"""
# client = Client('http://lg-11-152.ko.cn:50070')
client=InsecureClient('http://lg-11-152.ko.cn:50070',user='kzcq')
print (dir(client))
# filePath='/user/kzcq/data_in_parquet/phone_game_user_info/date=2018-05-14/part-00000-ef419a27-042e-4690-8a33-774539d6c31f.c000.snappy.parquet'
filePath = '/user/kzcq/datatest/test.json'
jsondata = {"@timestamp": "2018-05-22T02:51:32.392Z",
        "beat": {"hostname": "lg-13-135.ko.cn", "name": "lg-13-135.ko.cn", "version": "5.5.0"}, "input_type": "log",
        "message": "120|0|kongzhong_2034115|120|0|0|22|HUAWEI BND-AL10|866369034951568|null|1920x1080|Android|Android OS 7.0 / API-24 (HONORBND-AL10/C00B182)|2018-01-31 23:59:42 +0800|LOGIN|3|117.136.45.98|3|0|null|null|利海德·布德料|671917245932748800|12010A4E0010022100|671917245932748800",
        "offset": 10390, "source": "/data/0521/120.game.login.2018-02-01", "type": "log"}
import json
js=json.dumps(jsondata)

# with client.read(filePath) as fs:
    # content=pd.read_parquet(fs,engine='fastparquet')
    # content=pd.read_parquet('example_pa.parquet', engine='pyarrow')
    # print(content)
with client.write(filePath) as fs:
    fs.write(js)


# 关于python操作hdfs的API可以查看官网:
# https://hdfscli.readthedocs.io/en/latest/api.html
# import sys
# from hdfs.client import Client
#
# #设置utf-8模式
# reload(sys)
# sys.setdefaultencoding( "utf-8" )

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

# client = Client(url, root=None, proxy=None, timeout=None, session=None)
# client = Client("http://hadoop:50070")

# move_or_rename(client,'/input/2.csv', '/input/emp.csv')
# read_hdfs_file(client,'/input/emp.csv')
# put_to_hdfs(client,'/home/shutong/hdfs/1.csv','/input/')
# append_to_hdfs(client,'/input/emp.csv','我爱你'+'\n')
# write_to_hdfs(client,'/input/emp.csv','我爱你'+'\n')
# read_hdfs_file(client,'/input/emp.csv')
# move_or_rename(client,'/input/emp.csv', '/input/2.csv')
# mkdirs(client,'/input/python')
# print list(client,'/input/')
# chown(client,'/input/1.csv', 'root')