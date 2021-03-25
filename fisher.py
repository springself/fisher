# 路由的另一种注册方式
# app.add_url_rule('/hello', view_func=hello)
from app import create_app

app = create_app()
# print(__name__)
if __name__ == '__main__':
    # print(id(app), '启动')
    app.run(host=app.config['HOST'], debug=app.config['DEBUG'], port=app.config['PORT'])
