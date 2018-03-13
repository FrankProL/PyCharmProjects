# encoding:utf-8

from impala.dbapi import connect 
conn = connect(host='lg-15-163.ko.cn',port=21050)
cur = conn.cursor()
cur.execute('show tables')
print cur.fetchall()
cur.close()
conn.close()