#!/usr/bin/env python
#-*- coding: utf-8 -*-

import MySQLdb

# 打开数据库
db = MySQLdb.connect("10.0.0.101","root","redhat","test001")
# 使用cursor()方法获取数据
cursor = db.cursor()
# sql语句插入
sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME,AGE,SEX,INCOME) \
       VALUES('%s','%s','%d','%c','%d')" % \
       ('Jeff','Lee',26,'M',8000)
try:
    cursor.execute(sql)
    db.commit()
    print "Data insert successfully."
except:
    db.rollback()

# 关闭数据库
db.close()
