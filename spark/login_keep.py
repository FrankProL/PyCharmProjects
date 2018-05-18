#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/16 15:57
# @Author  : Frank
# @Site    : 
# @File    : login_keep.py
# @Software: PyCharm
"""

import pandas as pd

# df=pd.read_csv('login_data.csv',sep=',',header=0,encoding='utf-8')
# print (df[df['loginDay']=='2018-05-16'])
# df_11=df[df['loginDay']=='2018-05-11']

df=pd.read_csv('login_data.csv',sep=',',header=0,encoding='utf-8',index_col='loginDay')
# print (df['2018-05-11':'2018-05-11'].groupby(['guid']).count())
df_11=df['2018-05-11':'2018-05-11'].drop_duplicates(subset='guid')
df_14=df['2018-05-14':'2018-05-14'].drop_duplicates(subset='guid')

tmp=pd.merge(df_11,df_14,how='left',on='guid')
tmp.columns=['guid','login','keep']
tmp['3_keep']=(tmp['keep']>0)
print (tmp[['guid','login','3_keep']])