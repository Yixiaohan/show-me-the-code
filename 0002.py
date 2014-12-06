# -*- coding:utf8 -*-
# Source:https://github.com/renzongxian/show-me-the-code
# Author:renzongxian
# Date:2014-12-06
# Python 2.7, MySQL-python does not currently support Python 3

"""

做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
使用 Python 如何生成 200 个激活码（或者优惠券）？

"""

import uuid
import MySQLdb


def generate_key():
    key_list = []
    for i in range(200):
        uuid_key = uuid.uuid3(uuid.NAMESPACE_DNS, str(uuid.uuid1()))
        key_list.append(str(uuid_key).replace('-', ''))
    return key_list


def write_to_mysql(key_list):
    # 打开数据库连接
    db = MySQLdb.connect("localhost", "test", "test1234", "testDB")

    # 使用cursor()方法打开操作游标
    cursor = db.cursor()

    # 如果数据表已存在，删除表
    cursor.execute("drop table if exists ukey")

    # 创建数据表SQL语句
    sql = """create table ukey (
            key_value char(40) not null
            )"""
    cursor.execute(sql)

    # SQL 插入
    try:
        for i in range(200):
            cursor.execute('insert into ukey values("%s")' % (key_list[i]))
        # 提交到数据库执行
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()

    # 关闭数据库
    db.close()


if __name__ == '__main__':
    write_to_mysql(generate_key())
