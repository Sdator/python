
# -*- coding: utf-8 -*-

import requests


def 爬取(提交地址, 请求数据, 返回格式="str", 是否使用代理=0):
    """`参数1` 提交地址

    `参数2` 请求数据

    `参数3` 返回格式 `str`返回文本格式，`json`返回字典对象  `默认为返回文本`

    `参数3` 是否使用代理 `0`=不使用, `1`=使用 开启后需要自己设置一下梯子的相关IP和端口 `默认为不使用`
    """

    代理 = ""

    if 是否使用代理:
        # 你的梯子
        代理 = {
            "http": "http://127.0.0.1:10001",
            "https": "http://127.0.0.1:10001",
        }

    # 提交地址 不要这么明显
    请求头 = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
    # 访问网站
    r = requests.get(提交地址, params=请求数据, headers=请求头, proxies=代理)

    # 返回文本类型还是json
    sTmp = ""
    if 返回格式 == "str":
        sTmp = r.text
    else:
        sTmp = r.json()

    return sTmp


class base:
    def __init__(self):
        self.请求头 = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
        self.代理 = {
            "http": "http://127.0.0.1:10001",
            "https": "http://127.0.0.1:10001",
        }
        self.是否使用代理 = 0


class net():

    def __init__(self, url=""):
        self.url = url

    @property
    def 取回数据(self):
        return self._取回数据

    @property
    def 请求头(self):
        return self._请求头

    @property
    def 代理(self):
        return self._代理

    @property
    def 是否使用代理(self):
        return self._是否使用代理

    @是否使用代理.setter
    def 是否使用代理(self, value):
        if not value:  # 如果不是用代理就清空
            self.代理 = None
        self._是否使用代理 = value

    def _请求(self, url, 是否使用代理=0, **kwargs):
        self.是否使用代理 = 是否使用代理
        r = requests.get(url or self.url,  headers=self.请求头,
                         proxies=self.代理, **kwargs)
        return r

    @staticmethod
    def 读地址文本内容(self, url, **kwargs):
        r = self._请求(url, **kwargs)
        self._取回数据 = r.text
        return self._取回数据


if __name__ == "__main__":

    txt = net.读地址文本内容("https://ngosang.github.io/trackerslist/trackers_all_ip.txt",
                      是否使用代理=1)

