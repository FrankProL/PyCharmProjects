#coding=utf8
import re
import requests
import random

import sys

"""从百度图片下载人物图片
"""
def spiderPic(html,keyword):
    print ('now is finding:'+keyword+' ，downloading now and please wait...')
    iter=range(200).__iter__()
    for addr in re.findall('"objURL":"(.*?)",',html,re.S):
        print ('now spider is finding addrs is:'+str(addr)[0:30]+'...')
        try:
            pics = requests.get(addr, timeout=10)
        except requests.exceptions.ConnectionError:
            print ('error caught some wrong thing')
            continue
        # fp = open((keyword+'_'+str(random.randrange(0, 1000, 4)) + '.jpg').decode('utf-8'),'wb')
        fp = open((keyword + '_' + str(iter.next()) + '.jpg').decode('utf-8'), 'wb')
        fp.write(pics.content)
        fp.close()

if __name__ == '__main__':
    word = raw_input("输入你想要爬的文字: ")
    result = requests.get('http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word='+word)
spiderPic(result.text,word)
