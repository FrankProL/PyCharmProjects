#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/22 10:54
# @Author  : Frank
# @Site    : 
# @File    : spark_read.py
# @Software: PyCharm
"""
from pyspark.sql import SparkSession

# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
# export PYTHONIOENCODING=utf8
import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)


spark=SparkSession.builder.appName("Python Spark SQL basic example").getOrCreate()

# df=spark.read.parquet("/user/kzcq/data_in_parquet/phone_game_user_info")
# df=spark.read.parquet("/user/kzcq/data_in_parquet/phone_game_userlogin_guest")
# df=spark.read.parquet("/user/kzcq/data_in_parquet/phone_game_userlogin_kong")
# df=spark.read.parquet("/user/kzcq/data_in_parquet/phone_game_userlogin_tripartite")
# df=spark.read.json('file:///usr/local/spark-2.3.0/examples/src/main/resources/people.json')
df=spark.read.parquet('/user/kzcq/datalogintest2/')
df.show(30)

# df.createOrReplaceTempView('user')
# users=spark.sql('select * from user')
# users.show()
# df.write.parquet('/user/kzcq/data_in_parquet/test')
# df.write.json('/user/kzcq/data_in_parquet/test')
# df.printSchema()

spark.stop()