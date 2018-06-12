#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/11 17:14
# @Author  : Frank
# @Site    : 
# @File    : quick_start.py
# @Software: PyCharm
"""
from pyspark.sql import SparkSession

spark=SparkSession.builder.appName('quickStart').getOrCreate()


textFile=spark.read.text('file:///usr/local/spark-2.3.0/README.md')

textFile.count()  # Number of rows in this DataFrame
textFile.first()  # First row in this DataFrame

linesWithSpark = textFile.filter(textFile.value.contains("Spark"))
textFile.filter(textFile.value.contains("Spark")).count()  # How many lines contain "Spark"?


from pyspark.sql.functions import *

textFile.select(size(split(textFile.value, "\s+")).name("numWords")).agg(max(col("numWords"))).collect()
wordCounts = textFile.select(explode(split(textFile.value, "\s+")).alias("word")).groupBy("word").count()

textFile.select(explode(split(textFile.value, "\s+")).alias('words')).groupBy('words').count().sort('count').show()
textFile.select(explode(split(textFile.value, "\s+")).name('words')).groupBy('words').count().sort('count').show()
textFile.select(explode(split(textFile.value, "\s+")).alias('words')).groupBy('words').count().sort('count').collect()
