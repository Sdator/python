# -*- coding: utf-8 -*-
'''
by 绝 2019.4.15

所需模块：
    pip install requests
'''
import urllib.parse
from AirCom import *


# 用作参考 已在AirCom中用类实现了
def 吉儿不放假(页数):
    # 提交地址 不要这么明显
    url = base64.b64decode(
        b'aHR0cCUzQS8vbi4yeHd0NzUuY24vaW5kZXgucGhwL2luZGV4L2luZGV4L2hlemkuaHRtbA==')
    url = str(url, 'utf8')
    url = urllib.parse.unquote(url)
    print(url)
    # 访问数据
    提交数据 = {'page': 页数, 'userid': 10029, 'ddh': 'vA8RVMNwA2'}

    # 访问网站
    返回数据 = 爬取(url, 提交数据, "json")

    # 用来保存需要的数据
    data = {}
    # 如果数据存在
    if 返回数据:
        for v in 返回数据:
            print(v["id"])
            # 关联需要的数据
            data["url"] = v["url"]
            data["id"] = v["id"]
            data["date"] = v["shijian"]
            data["name"] = v["name"]
            # datas.append(data.copy())

            # 生成器
            yield data


def init():
    # 生成保存路径

    #日期 = datetime.now().strftime("%Y%m%d")
    #路径 = AirFile("/json/%s_H.json" % 日期)
    #路径.创建目录Ex()

    # 类实现 采用递归
    # jj = 吉吉儿不放假().返回数据

    # kk= geodreamer().返回数据
    kk= 老的().返回数据

    # 写出文件("不放假", jj)
    写出文件("不放假geo", kk)

    # 面向过程的实现方法 可以配合yield生成器
    # for num in range(1, 20):

    #     datas = 吉儿不放假(num)
    #     if not datas:
    #         break
    #     for d in datas:
    #         写出文件(路径.绝对路径, d)


if __name__ == '__main__':
    init()
