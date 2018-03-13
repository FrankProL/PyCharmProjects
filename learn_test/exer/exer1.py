#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
print os.getcwd()
import ttt.ttt

def ChangeInt( a ):
    a = 10

b = 2
ChangeInt(b)
print b # 结果是 2

 
# 可写函数说明
def changeme( mylist ):
   "修改传入的列表"
   mylist.append([1,2,3,4]);
   print "函数内取值: ", mylist
   return
 
# 调用changeme函数
mylist = [10,20,30];
changeme( mylist );
print "函数外取值: ", mylist



path='class.py'
print os.path.realpath(path)
dirname = os.path.dirname(os.path.realpath('__file__'))  
print dirname
path = os.path.join(dirname, path)  
print os.path.normpath(path) 

print os.getcwd() 
os.chdir("D:\logs" )
print os.getcwd() 
print os.path.realpath(path)
print os.path.realpath('__file__')  