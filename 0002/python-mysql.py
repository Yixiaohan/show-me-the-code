#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql


conn = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='pymysql')
try:
    with conn.cursor() as cursor:
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS active_code(code varchar(30));")
        with open('active_code.txt', "r") as f:
            while True:
                s = f.readline()
                if s == "":
                    break
                cursor.execute("INSERT INTO active_code VALUES (%s)", [s])

        conn.commit()

    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM active_code")
        data_2t = cursor.fetchall()
        for data_t in data_2t:
            for data in data_t:
                print(data)

finally:
    conn.close()
