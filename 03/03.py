from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
import random
import mysql.connector
#连接dexterliao
conn = mysql.connector.connect(user='root', password='', database='dexterliao')
cursor = conn.cursor()
#创建user表单
cursor.execute('create table user (`id` INT UNSIGNED AUTO_INCREMENT, `code` VARCHAR(40) NOT NULL,PRIMARY KEY ( `id` ))')
#sqlalchemy 连接mysql
engine = create_engine('mysql+mysqlconnector://root:@localhost:3306/dexterliao')

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(Integer, primary_key=True)
    code = Column(String(40))
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
# 创建session对象:
session = DBSession()
# 创建新User对象:
for i in range(200):
    new_code = User(id=(i+1), code=random.randint(10000000,99999999))
    session.add(new_code)


session.commit()
session.close()

