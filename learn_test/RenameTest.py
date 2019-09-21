#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/8/2 15:40
# @Author  : Frank
# @Site    : 
# @File    : RenameTest.py
# @Software: PyCharm
"""
import os
import re
# 文件批量重命名
# 正则匹配删除部分文件

# file=u'E:\Java学习资料\北风Java课程资料\课程十五、深入Java性能调优\资料'
# # print(os.listdir(file))
# for i in os.listdir(file):
#     if os.path.isdir(file+'\\'+i):              # 字符串拼接路径
#         # print (os.listdir(os.path.join(file,i)))  # 通过os.path.join()方法，直接将路径和文件名拼接
#         for fi in os.listdir(os.path.join(file,i)):
#             if re.search(r'.mmap$',fi):
#                 print(fi)
#                 os.rename(os.path.join(file,i,fi),os.path.join(file,i+fi))
#             if re.search(r'mmap.',fi):
#                 print (fi)
#                 os.remove(os.path.join(file,i,fi))
#         os.removedirs(os.path.join(file,i))

# 循环遍历目录下所有文件，查找指定类型文件，并复制到指定文件夹
import shutil   # 一个文件、目录的管理接口，提供了一些用于复制文件、目录的函数
file=ur"E:\Java学习资料\北风Java课程资料\深入Java性能调优\代码\33"
print(os.listdir(file))
def searchFile(curDire):
    for i in os.listdir(curDire):
        if os.path.isdir(os.path.join(curDire,i)):
            searchFile(os.path.join(curDire,i))
        else:
            if re.search(r'\.java',i):
                shutil.copy(os.path.join(curDire,i),"E:\javafile"+"\\"+i)
                print(i)
if __name__ == '__main__':
    searchFile(file)