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

client=Client('http://lg-11-152.ko.cn:50070')
print (dir(client))
filePath='/user/kzcq/data_in_parquet/phone_game_user_info/date=2018-05-14/part-00000-ef419a27-042e-4690-8a33-774539d6c31f.c000.snappy.parquet'
with client.read(filePath) as fs:
    content=pd.read_parquet(fs,engine='pyarrow')
    print(content)