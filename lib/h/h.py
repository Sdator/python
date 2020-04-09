# -*- coding: utf-8 -*-

# import os
# import base64
# import urllib.parse
from abc import ABCMeta, abstractmethod
from lib.net.base import 爬取
import json


class H:
    __metaclass__ = ABCMeta

    def __init__(self):
        pass
    # 虚函数
    @abstractmethod
    def 提交数据(self):
        pass

    @abstractmethod
    def url(self):
        pass


class 吉吉儿不放假(H):
    返回数据 = []
    页数 = 0
    i = 0

    @property
    def 递增页数(self):
        self.页数 += 1
        return self.页数

    @property
    def __递增(self):
        self.i += 1
        return self.i

    def __init__(self):
        self.获取()

    def __str__(self):
        return json.dumps(self.返回数据, ensure_ascii=False)

    def 获取(self):
        # 访问网站
        返回数据 = 爬取(self.url, self.提交数据, "json")

        # 如果数据不存在返回  自动提取所有数据为止
        if not 返回数据:
            return

        # 用来保存需要的数据
        data = {}
        for v in 返回数据:
            print(v["id"])
            # 关联需要的数据
            data["序号"] = self.__递增
            data["url"] = v["url"]
            data["id"] = v["id"]
            data["date"] = v["shijian"]
            data["name"] = v["name"]

            self.返回数据.append(data.copy())
        # 递归
        self.获取()


class geodreamer(吉吉儿不放假):
    @property
    def 提交数据(self):
        return {'page': self.递增页数, 'userid': 10109, "ddh": 'qyDBPSs7FZ'}

    @property
    def url(self):
        url = "http://fdgdfgdfgdfgdfshtyjykj.geodreamer.xyz/index.php/index/index/hezi.html"
        return url


class 老的(吉吉儿不放假):
    @property
    def 提交数据(self):
        return {'page': self.递增页数, 'userid': 10029, 'ddh': 'vA8RVMNwA2'}

    @property
    def url(self):
        url = "http://gt57jip.cn/index.php/index/index/hezi.html"
        return url
