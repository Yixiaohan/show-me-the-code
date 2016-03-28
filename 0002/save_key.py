#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
"""
import MySQLdb
import string
import random

KEY_LEN = 20
KEY_ALL = 200

def base_str():
    return (string.letters+string.digits)

def key_gen():
    keylist = [random.choice(base_str()) for i in range(KEY_LEN)]
    return ("".join(keylist))

def key_num(num,result=None):
    if result is None:
        result = []
    for i in range(num):
        result.append(key_gen())
    return result

class mysql_init(object):

    def __init__(self,conn):
        self.conn = None

    #connect to mysql
    def connect(self):
        self.conn = MySQLdb.connect(
	    host = "localhost",
            port = 3306,
            user = "root",
            passwd = "123456",
            db = "test",
            charset = "utf8"    	
	)

    def cursor(self):
        try:
            return self.conn.cursor()
        except (AttributeError,MySQLdb.OperationalError):
            self.connect()
            return self.conn.cursor()

    def commit(self):
        return self.conn.commit()

    def close(self):
        return self.conn.close()
    
def process():
    dbconn.connect()
    DropTable()
    CreateTable()
    InsertDatas()
    QueryData()
    dbconn.close()

def execute(sql):
    '''执行sql'''
    conn=dbconn.cursor()
    conn.execute(sql)

#def executemany(sql, tmp):
#    '''插入多条数据'''
#    conn=dbconn.cursor()
#    conn.executemany(sql,tmp)

def query(sql):
    '''查询sql'''
    conn=dbconn.cursor()
    conn.execute(sql)
    rows = conn.fetchmany(10)
    return rows

def DropTable():
    conn=dbconn.cursor()
    conn.execute("DROP TABLE IF EXISTS `user_key`")
     
def CreateTable():
    conn=dbconn.cursor()
    sql_create =''' CREATE TABLE `user_key` (`ID` int(5) NOT NULL auto_increment,`key` varchar(100) NOT NULL,PRIMARY KEY (`ID`))'''
    conn.execute(sql_create)

def InsertDatas():
    conn=dbconn.cursor()
    insert_sql = "insert into user_key(key) values(%s)"
    key_list = key_num(KEY_ALL)
    print len(key_list)
    conn.executemany(insert_sql,key_list)

def DeleteData():
    del_sql = "delete from user_key where id=2"
    execute(del_sql)

def QueryData():
    sql = "select * from user_key"
    rows = query(sql)
    printResult(rows)

def printResult(rows):
    if rows is None:
        print "rows None"
    for row in rows:
        print row

if __name__ == "__main__":
   dbconn = mysql_init(None) 
   process()
