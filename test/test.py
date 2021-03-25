# s = '123456-7'
# print(s.isdigit())
# s = s.replace('-', '')
#
# print(s)
# q = '1234567890-'
# isbn_or_key = 'key'
# if len(q) == 13 and q.isdigit():
#     isbn_or_key = 'isbn'
#     short_q = q.replace('-', '')
# elif '-' in q and len(short_q) == 10 and short_q.isdigit():
#     isbn_or_key = 'isbn'
# print(isbn_or_key)
arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
# arr1.sort()
# print(arr1)
# # arr1.pop(2)
# arr1[::-1]
# print(arr1[::-1])
#
# print(arr1.index(2))
# #
# print(arr1[::-1].index(2))

# dic = {1: 3, 2: 5}
# print(dic[4])
# arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
# from collections import Counter
# arr1 = Counter(arr1)
# print(arr1)
# import sys
# print(sys.path)

# print(__name__)
from flask import Flask, current_app, request
app = Flask(__name__)
# 离线应用、单元测试
ctx = app.app_context()
ctx.push()
a = current_app
b = current_app.config['DEBUG']
ctx.pop()

# with语句
with app.app_context():
    a = current_app
    b = current_app.config['DEBUG']
# 可以对一个实现了上下文协议的对象使用with
# 上下文管理器
# __enter__  __exit__
# 上下文表达式必须返回一个上下文管理器

class MyResource():
    def __enter__(self):
        print('connection to resource')
        return self
    def __exit__(self, exc_type, exc_value, tb):
        if exc_type:
            print('process exception')
        else:
            print('no exception')
        print('close resource connection')
        return True
    def query(self):
        print('query data')
try:
    with MyResource() as resource:
        1/0
        resource.query()
except:
    print('outter exception')

