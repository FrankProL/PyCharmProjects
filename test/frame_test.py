#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/3/22 13:52
# @Author  : Frank
# @Site    : 
# @File    : frame_test.py
# @Software: PyCharm
"""
import pandas as pd

left1= pd.DataFrame({'key':['a','b','a','a','b','c'],'value':range(6)})
right1=pd.DataFrame({'group_val':[3.5,7]},index=['a','b'])

print (left1)
print ('==================')
print (right1)

print pd.merge(left1,right1,left_on='key',right_index=True)