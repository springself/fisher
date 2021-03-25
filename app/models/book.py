# sqlalchemy
# flask_sqlalchemy
# 基础类都是从sqlalchemy中导入的
from sqlalchemy import Column, Integer, String
# 使用flask封装的sqlalchemy
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    # nullable = False 不能为空
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='未名')
    isbn = Column(String(15), nullable=False, unique=True)
    price = Column(String(20))
    binding = Column(String(20))  # 书籍装帧，精装/平装
    pages = Column(Integer)
    publisher = Column(String(50))
    pubdate = Column(String(20))
    summary = Column(String(1000))  # 简介
    image = Column(String(50))

    def sample(self):
        pass
