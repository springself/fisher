import requests


class HTTP:
    @staticmethod
    def get(url, return_json=True):
        '''

        :param url:
        :param return_json: 增强了get方法的通用性
        :return:
        '''
        r = requests.get(url)
        # restful要求返回结果是json格式的
        # 如果调用的API返回结果是json格式的，可以直接调用r.json()返回
        # if r.status_code == 200:
        #     if return_json:
        #         return r.json()
        #     else:
        #         # 返回原始的字符串
        #         return r.text
        # else:
        #     if return_json:
        #         return {}
        #     else:
        #         return ''
        # python中的三元表达式
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text


