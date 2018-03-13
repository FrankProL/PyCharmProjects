# encoding:utf-8
import MySQLdb
import json

into_db=("172.23.15.19","loujianfeng","o8Jy4QqqHk4WytL","utf8")  

# 连接到MySQL  
cnxn = MySQLdb.connect(host=into_db[0], user=into_db[1], passwd=into_db[2], charset=into_db[3],db='stats_dev')           
 
sql = "select uid,mobilephone,nickname from tmp_result_1127_l limit 13"

# 通过cursor创建游标
cursor = cnxn.cursor()  

# 执行数据查询                                                          
cursor.execute(sql)                                                            
  
# 提交事物      
# cnxn.commit()                                                 

#fetchone() 用于查询单条数据。
print (cursor.fetchone())			
print (repr(cursor.fetchone()).decode('unicode-escape'))


#fetchall() 用于查询多条数据。
# for x in cursor.fetchall():			
# 	print json.dumps(x, encoding="utf-8", ensure_ascii=False)

for uid in cursor.fetchall():			
	print json.dumps(uid, encoding="utf-8", ensure_ascii=False)

cursor.close()
cnxn.close()

names = 'aramis', 'athos','porthos'
print names


