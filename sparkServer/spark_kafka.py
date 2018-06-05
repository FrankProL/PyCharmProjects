#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/1 19:40
# @Author  : Frank
# @Site    : 
# @File    : spark_kafka.py
# @Software: PyCharm
"""
from __future__ import print_function

import sys

from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split

if __name__ == "__main__":
    # if len(sys.argv) != 4:
    #     print("""
    #     Usage: structured_kafka_wordcount.py <bootstrap-servers> <subscribe-type> <topics>
    #     """, file=sys.stderr)
    #     exit(-1)
    #
    # bootstrapServers = sys.argv[1]
    # subscribeType = sys.argv[2]
    # topics = sys.argv[3]
    bootstrapServers='172.23.11.150:9092'
    subscribeType='subscribe'
    topics='kzmg_hunter_login'

    spark = SparkSession\
        .builder\
        .appName("StructuredKafka")\
        .getOrCreate()

    # Create DataSet representing the stream of input lines from kafka
    lines = spark\
        .readStream\
        .format("kafka")\
        .option("kafka.bootstrap.servers", bootstrapServers)\
        .option(subscribeType, topics)\
        .load()\
        .selectExpr("CAST(value AS STRING)")

    # # Split the lines into words
    # words = lines.select(
    #     # explode turns each item in an array into a separate row
    #     explode(
    #         split(lines.value, ' ')
    #     ).alias('word')
    # )
    #
    # # Generate running word count
    # wordCounts = words.groupBy('word').count()
    #
    # # Start running the query that prints the running counts to the console
    # query = wordCounts\
    #     .writeStream\
    #     .outputMode('complete')\
    #     .format('console')\
    #     .start()
    #
    # query.awaitTermination()

    # query=lines.writeStream.format('console').start()
    # query.awaitTermination()

    query =lines.writeStream.format('json')\
        .outputMode('append')\
        .option("checkpointLocation", "/user/kzcq/datalogintest3").option('path','/user/kzcq/datalogintest2').start()
    query.awaitTermination()