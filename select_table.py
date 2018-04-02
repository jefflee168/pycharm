#!/usr/bin/env python
#-*- coding: utf-8 -*-

import MySQLdb

# 打开数据库
db = MySQLdb.connect("10.0.0.101","root","redhat","test001")
# 使用cursor()方法获取游标
cursor = db.cursor()
# sql查询语句
sql="SELECT * FROM EMPLOYEE WHERE INCOME > '%d'" % (1000)

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
              (fname,lname,age,sex,income)
except:
    db.rollback()

#据库
db.close()