#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/3/22 14:19
# @Author  : Frank
# @Site    : 
# @File    : user_account_merge.py
# @Software: PyCharm
"""
import pandas as pd

useraccount=pd.read_csv('user_account.csv',sep=',',encoding='utf-8',header=0)
# print useraccount['user_rank'][useraccount['user_rank'].isnull()]     # 查找缺失值
useraccount=useraccount.dropna()                                        # 对缺失值处理后才能进行类型转换
useraccount['user_rank']=useraccount['user_rank'].astype(long)
print useraccount.ix[1:10,:]

log=pd.read_csv('log.csv',sep=',',encoding='utf-8',header=0,dtype={'log1':str})    #
print type(log['log1'][0])
print log.ix[1:10,:]

log2=pd.read_csv('log2.csv',sep=',',encoding='utf-8',header=0,dtype={'log1':str})    #
print type(log['log1'][0])
print log.ix[1:10,:]

new=pd.merge(useraccount,log,how='left',on='user_id')
new2=pd.merge(new,log2,how='left',on='user_id')
new2=new2.fillna(0)
new2.to_csv('merge_result.csv',sep=',',encoding='utf-8',index=False)
