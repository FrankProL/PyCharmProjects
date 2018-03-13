#! /usr/bin/env python  
# -*- coding: utf-8 -*-  

'''
python 2.X版本的中文编码一直是一个头疼的事，这里主要解决中文列表或者字典的中文输出打印
'''
import json 

dic = {"course":"我爱python"}  
print dic  
#转化成json输出  
print json.dumps(dic,encoding="utf-8",ensure_ascii=False)  
#{"course": "我爱python"}  
  
list = ["我","python","学习"]  
print list  
#分别输出  
for s in list:  
    print s #分别为中文  
#通过转化json.dumps输出  
print json.dumps(list, encoding="utf-8", ensure_ascii=False)  
#["我", "python", "学习"]  

print '============================='
# ----------------------------------
# 对于 obj = [u'\u7ef3\u5b50', u'\u5e26\u5b50'] 这种情况， 使用：print(repr(obj).decode('unicode-escape'))
print(repr(list).decode('unicode-escape'))
print(repr(dic).decode('unicode-escape'))

# 对于 obj = ['绳子','带子'] 这种情况，使用：print(repr(obj).decode('string-escape'))
print(repr(list).decode('string-escape'))
print(repr(dic).decode('string-escape'))