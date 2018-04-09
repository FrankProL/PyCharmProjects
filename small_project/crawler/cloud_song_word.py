#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/4/8 9:42
# @Author  : Frank
# @Site    : 
# @File    : cloud_song_word.py
# @Software: PyCharm
"""
import requests
from bs4 import BeautifulSoup
import json
import re

# """调用api，根据歌曲id获取歌词"""
# lrc_url = 'http://music.163.com/api/song/lyric?' + 'id=' + str(191232) + '&lv=1&kv=1&tv=-1'
# lyric = requests.get(lrc_url)
# json_obj = lyric.text
# j = json.loads(json_obj)
# lrc = j['lrc']['lyric']
# pat = re.compile(r'\[.*\]')
# lrc = re.sub(pat, "", lrc)
# lrc = lrc.strip()
# print(lrc)


# 添加headers和反盗链referer以模拟浏览器，防止被网站拒绝访问
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'Referer': 'http://music.163.com/',
        'Host': 'music.163.com'}


# """通过歌手id，获取歌曲id列表"""
# singer_url = 'http://music.163.com/artist?id=' + str(6731)
# web_data = requests.get(singer_url,headers=headers)
# soup = BeautifulSoup(web_data.text, 'lxml')
# singer_name = soup.select("#artist-name")
# r = soup.find('ul', {'class': 'f-hide'}).find_all('a')
# r = (list(r))
# music_id_set=[]
# for each in r:
#     song_name = each.text  # print(each.text)
#     song_id = each.attrs["href"]
#     music_id_set.append(song_id[9:])
# print(music_id_set)


top50_singer_url = 'http://music.163.com/playlist?id=119712779'
web_data = requests.get(top50_singer_url,headers=headers)

soup = BeautifulSoup(web_data.text, 'lxml')

R = soup.textarea.text  # 找到歌手ID所在的标签
print R
json_obj = json.loads(R)
top50_singer_ID_set = []
for each in json_obj:
    singer_ID = each['artists'][0]['id']
    top50_singer_ID_set.append(singer_ID)  # 将排名前50的歌手的id存进一个列表
print(top50_singer_ID_set)


# def func(singer_ID1):  # 定义一个函数，通过一个歌手的id下载其最火的五十首歌的全部歌词
#
#
#     from bs4 import BeautifulSoup
#     singer_url = 'http://music.163.com/artist?id=' + str(singer_ID1)
#     web_data = requests.get(singer_url)
#     soup = BeautifulSoup(web_data.text, 'lxml')
#     singer_name = soup.select("#artist-name")
#
#     singer_name = singer_name[0].get('title')
#
#     r = soup.find('ul', {'class': 'f-hide'}).find_all('a')
#     r = (list(r))
#     music_id_set = []
#     music_name_set = []
#     for each in r:
#         song_name = each.text  # print(each.text)
#         music_name_set.append(song_name)
#
#         song_id = each.attrs["href"]
#         music_id_set.append(song_id[9:])
#
#     dic = dict(map(lambda x, y: [x, y], music_name_set, music_id_set))  # 将音乐名字和音乐id组成一个字典
#
#     from bs4 import BeautifulSoup
#     def get_lyric_by_music_id(music_id):  # 定义一个函数，通过音乐的id得到歌词
#         lrc_url = 'http://music.163.com/api/song/lyric?' + 'id=' + str(music_id) + '&lv=1&kv=1&tv=-1'
#
#         lyric = requests.get(lrc_url)
#         json_obj = lyric.text
#         # print(json_obj)
#         j = json.loads(json_obj)
#         # print(type(j))#打印出来j的类型是字典
#         try:  # 部分歌曲没有歌词，这里引入一个异常
#             lrc = j['lrc']['lyric']
#             pat = re.compile(r'\[.*\]')
#             lrc = re.sub(pat, "", lrc)
#             lrc = lrc.strip()
#             return lrc
#         except KeyError as e:
#             pass
#
#     x = 0
#     for i in music_id_set:
#         x = x + 1
#
#         print(x)
#         top_50_lyric = get_lyric_by_music_id(i)
#
#         f = open("F:/projects/scrapy/%s.txt" % singer_name, "ab")  # 单个文件存储一个歌手的50首热门歌曲的歌词并以歌手的名字命名
#         try:  # 引入异常
#             f.write(top_50_lyric.encode('utf-8'))
#
#             f.close()
#         except AttributeError as e2:
#             pass
#
#
# for singer_ID in top50_singer_ID_set:  # 依次将列表中的id代表的歌手的歌词下载下来
#     singer_ID1 = singer_ID
#     func(singer_ID1)
