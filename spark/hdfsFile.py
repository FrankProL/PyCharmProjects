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
import pandas as pd
"""通过hdfs client读取hdfs文件
https://hdfscli.readthedocs.io/en/latest/quickstart.html#instantiating-a-client
    通过pandas的read_parquet读取parquet文件，pandas 0.21 introduces new functions for Parquet:
https://pandas.pydata.org/pandas-docs/version/0.21/io.html#io-parquet
    需要使用pyarrow或fastparquet模块辅助，但都没安装成功，pyarrow提示和ipaddress模块冲突，fastparquet下载太慢、下载不下来
"""
client=Client('http://lg-11-152.ko.cn:50070')
print (dir(client))
filePath='/user/kzcq/data_in_parquet/phone_game_user_info/date=2018-05-14/part-00000-ef419a27-042e-4690-8a33-774539d6c31f.c000.snappy.parquet'
with client.read(filePath) as fs:
    content=pd.read_parquet(fs,engine='fastparquet')
    # content=pd.read_parquet('example_pa.parquet', engine='pyarrow')
    print(content)