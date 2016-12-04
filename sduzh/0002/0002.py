#!/usr/bin/python
# -*- coding: utf-8 -*-
# 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。

import MySQLdb 
from gencode import create_code

db = MySQLdb.connect(user="root", passwd="zhuming9011", db="show_me_the_code")
cursor = db.cursor()

try:
	cursor.executemany("INSERT INTO tb_0002(code) VALUES(%s)", create_code())
except MySQLdb.Error, e:
	print "MySQL Error %d: %s" %(e.args[0], e.args[1])

db.commit()
cursor.close()
db.close()


