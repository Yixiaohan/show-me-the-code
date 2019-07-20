import random
import string
import pymysql
from warnings import filterwarnings
filterwarnings("error",category=pymysql.Warning)  #  指定过滤告警的类别为 pymysql.Warning类，
db=pymysql.connect('localhost','root','Mr.jingcheng','python_db')
cur=db.cursor()
sql = """CREATE TABLE IF NOT EXISTS ALL_KEYS (
             V_KEY  CHAR(35) PRIMARY KEY,
             AVAIL  CHAR(1) 
             )"""



def insert_to_mysql(key):
    sql = "INSERT INTO ALL_KEYS(V_KEY,AVAIL) VALUES ('%s', '1')"%(key)
    try:
        cur.execute(sql)
        db.commit()
    except:
        print('无法插入')
        db.rollback()

def genernate_key(number=5, lenth=8, part=4):
    result = []
    char_set = string.ascii_letters + string.digits
    for i in range(0, number):
        key = ''
        for j in range(0, part):
            for k in range(0, lenth):
                key = key + random.choice(char_set)
            key = key + '-'
        key = key[0:-1]
        if key not in result:
            result.append(key)
            print("%s %s" % (str(i + 1), key))
        else:
            i -= 1
    return result

def key_read_avail():
    sql = "SELECT * FROM ALL_KEYS \
           WHERE AVAIL <> 0"
    cur.execute(sql)
    rows =cur.fetchall()
    result=[]
    for each in rows:
        result.append(each[0])
    return result

def key_read_all():
    sql = "SELECT * FROM ALL_KEYS"
    result = []
    try:
        cur.execute(sql)
        rows =cur.fetchall()
        for each in rows:
            result.append(each[0])
    except:
        print('错误：无法获取数据')
    return result

def verify_key(key):
    sql = "SELECT * FROM ALL_KEYS WHERE V_KEY='%s' AND AVAIL='1'"%key
    cur.execute(sql)
    res=cur.fetchone()
    if res is not None:
        try:
            cur.execute("UPDATE ALL_KEYS SET AVAIL = '0' WHERE V_KEY = '%s'" % (key))
            db.commit()
            return True
        except:
            print('错误！无法更新')
            db.rollback()
    else:
        return False



# result=genernate_key(200)
# for each in result:
#     insert_to_mysql(each)
print(verify_key('xGJDKbZw-0hfWuCbj-WyH6tAir-LawiPxvm'))
# result = key_read()
# key = 'yf56g7h8-cot4imw3-9e01gml1-0gy7xkdi'
# print(verify_key(result, key))
db.close()