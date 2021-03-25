from flask import jsonify, request

from . import web
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook

# print(id(app), '注册路由')
from ..forms.book import SearchForm

# print(__name__)
@web.route('/book/search')
def search():
    '''

    :param q: isbn or key
    :param page:
    :return:
    '''
    # request.args是不可变字典。可以调用to_dict()方法可以转换成可变字典
    # q = request.args['q']
    # page = request.args['page']
    form = SearchForm(request.args)
    if form.validate():
        # strip 去掉前后的空格
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page)
        # dict序列化
        # return json.dumps(result), 200, {'content-type':'application/json'}
        return jsonify(result)
    else:
        return jsonify(form.errors)
