#!/usr/bin/env python
#-*- coding: utf-8 -*-

import MySQLdb

# 打开数据库
db = MySQLdb.connect("10.0.0.101","root","redhat","test001")

# 使用 cursor方法获取操作游标
cursor = db.cursor()

# sql语句插入
sql = """CREATE TABLE EMPLOYEE(
         FIRST_NAME CHAR(20) NOT NULL,
         LAST_NAME CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT )"""
try:
    cursor.execute(sql)
    db.commit()
    print "INFO: Table create successfully."
except:
    db.rollback()

# 关闭数据库
db.close()
