#!/usr/bin/env python
# coding:utf-8

import MySQLdb

conn = MySQLdb.connect(host='127.0.0.1', user='root', db='flow', charset='utf8')
cur = conn.cursor()

sql = 'select * from xk_order_ready_5 where state=%d limit 5;'

cur.executemany(sql, (1000,))

print cur.fetchall()