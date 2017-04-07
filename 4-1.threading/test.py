#coding:utf-8
import MySQLdb

conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='', db='athena', charset='utf8')

cursor = conn.cursor()
sql ='select mobile from black_list;'

cursor.execute(sql)
result = cursor.fetchall()


black_list = [ i[0] for i in result ]
with open('s.txt', 'r') as fd:
    
    phone_list = [ line.strip() for line in fd ]

print list(set(black_list).intersection(set(phone_list)))
cursor.close()
conn.close()