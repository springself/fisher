# 第一个参数：蓝图的名称
# 第二个参数： 指定蓝图所在的包或者是模块
from flask import Blueprint

web = Blueprint('web', __name__)
from app.web import book
from app.web import user
# print(__name__)