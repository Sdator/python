# -*- coding: utf-8 -*-
'''
by 绝 2019.4.16

所需模块：
    pip install requests

'''


from AirCom import *


# https://www.ixigua.com/c/user/article/?user_id=50351072776&max_behot_time=0&max_repin_time=0&count=20&page_type=0
# https://www.ixigua.com/item/6675509335797269005/


# 用来保存所有数据
dataG = []
i = 0


def 李老师(用户名ID, 下一页=0, 加载的页数=20):
    # 提交地址 不要这么明显
    url = "https://www.ixigua.com/c/user/article/"

    请求数据 = {
        "user_id": 用户名ID,
        "max_behot_time": 下一页,
        "count": 加载的页数,
        "max_repin_time": 0,
        "page_type": 0
    }

    # 访问网站
    返回数据 = 爬取(url, 请求数据, "str")

    # 用来保存需要的数据
    data = {}
    # 获取下一页的ID
    下一页 = 返回数据["next"]["max_behot_time"]
    print(下一页)
    # 引用全局变量
    global i
    global dataG
    if 下一页:
        for v in 返回数据["data"]:
            i += 1
            data["序号"] = i
            data["标题"] = v["title"]
            data["阳光宽频网地址"] = v["display_url"]
            data["西瓜视频地址"] = 'https://www.ixigua.com'+v['source_url']
            # 由于append添加的只是引用会导致最后内容全一样，需要拷贝一个新对象来解决
            dataG.append(data.copy())
        # 递归
        李老师(用户名ID, 下一页)
    return


def init():
    # 老师有两个账户发布视频
    用户名id = [50351072776, 4234740937]
    for ID in 用户名id:
        李老师(ID)

    # 生成路径写出文件
    日期 = datetime.now().strftime("%Y%m%d")
    路径 = AirFile("/json/%s_李永乐老师视频.json" % 日期)
    路径.创建目录Ex()
    写出文件(路径.绝对路径, dataG)


if __name__ == '__main__':
    init()
