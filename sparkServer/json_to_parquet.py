#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/12 9:45
# @Author  : Frank
# @Site    : 
# @File    : json_to_parquet.py
# @Software: PyCharm
"""

from pyspark.sql import SparkSession

spark=SparkSession.builder.appName('json_to_parquet').getOrCreate()

