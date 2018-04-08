#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/4/8 10:38
# @Author  : Frank
# @Site    : 
# @File    : lrc_test.py
# @Software: PyCharm
"""
import requests
from bs4 import BeautifulSoup
import json
import re


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'Referer': 'http://music.163.com/',
        'Host': 'music.163.com'}


    try:
        response = requests.get(url,headers=headers)
        html=response.text
        return html
    except:
        print ('request errors')
        pass
def get_singer_info(html):
    soup=BeautifulSoup(html,'lxml')
    links=soup.find('ul',class_='f-hide').find_all('a')
    song_IDs=[]
    song_names=[]
    for link in links:
        song_ID=link.get('href').split('=')[-1]
        song_name=link.get_text()
        song_IDs.append(song_ID)
        song_names.append(song_name)
    return zip(song_names,song_IDs)

def get_lyric(song_id):
    url = 'http://music.163.com/api/song/lyric?' + 'id=' + str(song_id) + '&lv=1&kv=1&tv=-1'
    html=get_html(url)
    json_obj=json.loads(html)
    initial_lyric=json_obj['lrc']['lyric']
    regex=re.compile(r'\[.*\]')
    final_lyric=re.sub(regex,'',initial_lyric).strip()
    return final_lyric

def write_text(song_name,lyric):
    print (u'正在写入歌曲，{}'.format(song_name))
    # with open(u'{}.txt'.format(song_name),'a') as fp:
    #     fp.write(lyric)

if __name__ == '__main__':
    singer_id=input('请输入歌手id')
    start_url= 'http://music.163.com/artist?id={}'.format(singer_id)
    html=get_html(start_url)
    singer_infos=get_singer_info(html)
    print singer_infos
    for singer_info in singer_infos:
        lyric=get_lyric(singer_info[1])
        write_text(singer_info[0],lyric)