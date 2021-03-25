from flask import Flask

from app.models.book import db


def create_app():
    # Flask类里面，会根据此名字，找到app.py所在目录，即默认为根目录。
    app = Flask(__name__)
    # print(__name__, '<=====')
    # print(id(app), 'app的实例化')
    # 载入配置文件
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)
    db.init_app(app)
    # 第一种方案：
    # db.create_all(app=app)
    # 第二种方案：
    with app.app_context():
        db.create_all()
    return app


# 将蓝图注册到flask核心对象上
def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)
