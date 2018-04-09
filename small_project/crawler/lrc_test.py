#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/4/8 10:38
# @Author  : Frank
# @Site    : 
# @File    : lrc_test.py
# @Software: PyCharm
"""
"""
    1.找到正确的URL，获取源码；
    2.利用bs4解析源码，获取歌曲名和歌曲ID；
    3.调用网易云歌曲API，获取歌词；
    4.将歌词写入文件，并存入本地。
"""

import chardet
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
    try:
        json_obj=json.loads(html)
        initial_lyric=json_obj['lrc']['lyric']
        regex=re.compile(r'\[.*\]')
        final_lyric=re.sub(regex,'',initial_lyric).strip()
        return final_lyric
    except:
        print ('json异常------------'+url)
        final_lyric=url
        return final_lyric

def write_text(song_name,lyric):
    print (u'正在写入歌曲，{}'.format(song_name))
    with open(u'{}.txt'.format(song_name),'a') as fp:
        fp.write(lyric.encode('utf-8'))

if __name__ == '__main__':
    singer_id=input('请输入歌手id')
    start_url= 'http://music.163.com/artist?id={}'.format(singer_id)
    html=get_html(start_url)
    singer_infos=get_singer_info(html)
    print singer_infos
    for singer_info in singer_infos:
        lyric=get_lyric(singer_info[1])
        write_text(singer_info[0],lyric)

"""一般来说，网页上显示的URL就可以写在程序中，运行程序之后就可以采集到我们想要的网页源码。
    But在网易云音乐网站中，这条路行不通，因为网页中的URL是个假URL，真实的URL中是没有#号的
    
    利用requests、bs4、json和re模块来采集网易云音乐歌词，记得在程序中添加headers和反盗链referer以模拟浏览器，防止被网站拒绝访问。
    这里的get_html方法专门用于获取源码，通常我们也要做异常处理，未雨绸缪。
    
    获取到网页源码之后，分析源码，发现歌曲的名字和ID藏的很深，纵里寻她千百度，发现她在源码的294行，藏在<ul class="f-hide">标签下
    
    获取ID的时候需要对link进行切片处理，得到的数字便是歌曲的ID；另外，歌曲名是通过get_text()方法获取到的，
    最后利用zip函数将歌曲名和ID一一对应并进行返回
    
    得到ID之后便可以进入到内页获取歌词了，但是URL还是不给力
    找到了网易云音乐的API，只要把歌曲的ID放在API链接上便可以获取到歌词了
    
    在API中歌词信息是以json格式加载的，所以需要利用json将其进行序列化解析出来，并配合正则表达式进行清洗歌词
    
    http://baijiahao.baidu.com/s?id=1594746849107957374&wfr=spider&for=pc
"""