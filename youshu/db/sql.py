# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, Integer, BigInteger, TIMESTAMP, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from youshu import config

# 初始化数据库连接:
engine = create_engine(config.SQL_URI)
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
