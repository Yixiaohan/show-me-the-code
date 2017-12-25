from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine


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
# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id==5).one()
# 打印类型和对象的name属性:
print('type:', type(user))
print('name:', user.code)
# 关闭Session:
session.close()
