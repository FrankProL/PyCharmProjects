#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/4/16 9:36
# @Author  : Frank
# @Site    : 
# @File    : regular_test.py
# @Software: PyCharm
"""
""" re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
    re.search匹配整个字符串，直到找到一个匹配。
    re.sub用于替换字符串中的匹配项。
        re.sub(pattern, repl, string, count=0, flags=0)
            repl : 替换的字符串，也可为一个函数。
            count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
    re.compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
        re.compile() 返回 RegexObject 对象。
    re.findall在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
        注意： match 和 search 是匹配一次 findall 匹配所有。
    re.finditer和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。
    re.split方法按照能够匹配的子串将字符串分割后返回列表，它的使用形式如下：
        re.split(pattern, string[, maxsplit=0, flags=0])
    raw字符串（原始字符串，里面的字符不需要转义）    r'xxx'
        产生原因是ASCII 字符和正则表达式特殊字符间所产生的冲突。
        如果字符串中不带转义字符，则带不带r''，字符串的意思都是一样的。
"""
import re

print (re.match('www', 'www.baidu.com').start())  # 在起始位置匹配
print (re.match('www', 'www.baidu.com').end())  # 在起始位置匹配
print (re.match('www', 'www.baidu.com').span())  # 在起始位置匹配
print (re.match('com', 'www.baidu.com'))  # 不在起始位置匹配

print ('~~'*30)
line = 'Cats are smater than dogs ?'
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)
if matchObj:
    print (matchObj)
    print (matchObj.span())
    print ('matchObj.group() :'),
    print (matchObj.group())
    print ('matchObj.group(1) :'),
    print (matchObj.group(1))
    print ('mathcObj.group(2) :'),
    print (matchObj.group(2))
else:
    print('no match!')

print ('~~'*30)
print (re.search('www','www.baidu.com').span())
print (re.search('com','www.baidu.com').span())

searchObj=re.search(r'(.*) are (.*?) .*',line,re.M|re.I)
if searchObj:
    print ('searchObj.group() : '),
    print (searchObj.group())
    print ('searchObj.group(1) :'),
    print (searchObj.group(1))
    print ('searchObj.group(2) :'),
    print (searchObj.group(2))

print ('~~'*30)
matchObj = re.match(r'dogs', line, re.M | re.I)
if matchObj:
    print ("match --> matchObj.group() : ", matchObj.group())
else:
    print ("No match!!")

matchObj = re.search(r'dogs', line, re.M | re.I)
if matchObj:
    print ("search --> matchObj.group() : " + matchObj.group())
else:
    print ("No match!!")

print('~~'*30)
phone = "2004-959-559 # 这是一个国外电话号码"

# 删除字符串中的 Python注释
num = re.sub(r'#.*$', "", phone)
print ("电话号码是: "+ num)

# 删除非数字(-)的字符串
num = re.sub(r'\D', "", phone)
print ("电话号码是 : "+ num)

print ('~~'*30)
# 将匹配的数字乘以 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)

s = 'A28G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))

print ('~~'*30)
pattern = re.compile(r'\d+')  # 查找数字,匹配至少一个数字
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)

print(result1)
print(result2)

print('~~'*30)
it = re.finditer(r"\d+","12a32bc43jf3")
for match in it:
    print (match.group() )

print('~~'*30)
print (re.split('\W+', 'runoob, runoob, runoob.'))
print (re.split('(\W+)', 'runoob, runoob, runoob.'))
print (re.split('\W+', ' runoob, runoob, runoob.', 1) )
print (re.split('a*', 'hello world'))

# str.split不支持正则及多个切割符号，不感知空格的数量，比如用空格切割
s1="aa bb  cc,dd"
print(s1.split(" "))
# re.split，支持正则及多个字符切割
print(re.split(" +",s1))
print(re.split("[ ]",s1))
print(re.split("\s+",s1))   # \s匹配所有空白字符来切割（[\t\n\r\f\v]）  \S（任意非空白字符[^\t\n\r\f\v]
print(re.split("( +)",s1))  # 加括号将分割包括，则切分后列表保留分隔符
print(re.split("[\s,]+",s1)) # 多字符匹配，用中括号括起来


s = 'fadfdfa?.3\hello'
s1 = r'fadfafa\nhello'
print(re.split('\\\\',s))
print(re.split(r'\\',s))
# raw字符串
# 正则表达式使用反斜杆（\）来转义特殊字符，使其可以匹配字符本身，而不是指定其他特殊的含义
# 要匹配一个反斜杆本身，你也许要用'\\\\'来做为正则表达式的字符串，因为正则表达式要是\\，
# 而字符串里，每个反斜杆都要写成\\。