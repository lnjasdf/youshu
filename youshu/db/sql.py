# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, Integer, BigInteger, TIMESTAMP, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/growth')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建对象的基类:
Base = declarative_base()


class Info(Base):
    __tablename__ = 't_youshu'

    book_id = Column(BigInteger, primary_key=True)
    name = Column(String)
    author = Column(String)
    words = Column(String)
    last_time = Column(String)
    # create_time = Column(TIMESTAMP)
