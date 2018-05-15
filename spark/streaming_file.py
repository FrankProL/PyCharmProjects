#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/8 14:03
# @Author  : Frank
# @Site    : 
# @File    : streaming_file.py
# @Software: PyCharm
"""
from __future__ import print_function

import sys

from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split
if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("StructuredKafka") \
        .getOrCreate()

    # Create DataSet representing the stream of input lines from kafka
    lines = spark \
        .readStream \
        .option("sep",",")\
        .csv('/opt/modules/spark-2.3.0-bin-hadoop2.7/userdata/',"guid String,ip String,createTime String,userAccount String,region String")
    print(lines.isStreaming)
    lines.printSchema()
    lines.createTempView("tmp")
    count=spark.sql("select createTime ,count(guid) from tmp group by createTime order by createTime")
    query = count \
        .writeStream \
        .outputMode('complete') \
        .format('console') \
        .option('n','30') \
        .start()
    query.awaitTermination()
    # query=count.writeStream.format("csv") \
    #             .outputMode('update')\
    #             .option("checkpointLocation","/opt/modules/spark-2.3.0-bin-hadoop2.7/script" )\
    #             .option("path","/opt/modules/spark-2.3.0-bin-hadoop2.7/script").start()



