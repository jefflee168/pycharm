# -*- coding: utf-8 -*-

import MySQLdb

db = MySQLdb.connect("10.0.0.26","root","redhat","test001")

# 使用cursor来执行SQL语句
cursor = db.cursor()
cursor.execute("SELECT VERSION()")

# 使用cursor()来获取一条数据
data = cursor.fetchone()
print "Database version: %s " % data

# 关闭数据库
db.close()



