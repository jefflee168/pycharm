#!/usr/bin/env python
#-*- coding: utf-8 -*-

import MySQLdb

# 打开数据库
db = MySQLdb.connect("10.0.0.101","root","redhat","test001")
# 使用cursor()方法获取游标
cursor = db.cursor()
# sql更新
sql = "UPDATE EMPLOYEE SET INCOME = INCOME + 1000 WHERE INCOME = '%d'" % (8000)

try:
    cursor.execute(sql)
    db.commit()
    print "Data update successfully."
except:
    db.rollback()

# 关闭db.close()