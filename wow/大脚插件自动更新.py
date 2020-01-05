# -*- coding: utf-8 -*-
'''
by 绝 2019.10.6  QQ 250740270

本程序用于自动更新大脚插件

'''

# 网页
import requests
import json
import sys
import os
# 正则
import re
# 解包
import zipfile
# 组件
import tkinter as tk
from tkinter import filedialog
# 消息框
import tkinter.messagebox

# 弹窗
import ctypes


配置信息 = {
    "游戏路径": "",
    "当前版本": "1.13.2.18",
    "线程": 10,
    "历史": ['http://wow.bfupdate.178.com/BigFoot/Interface/classic/Interface.1.13.2.18.zip', ]
}

# 获取当前脚本路径
# path1 = sys.path[0]

# 组合合法路劲再打开文件
配置文件 = os.path.normcase('配置.json')

# 文件不存在创建
if not os.path.isfile(配置文件):
    with open(配置文件, "a", encoding='utf-8') as json_file:
        pass

# 读入配置
# 以utf8打开文件 并转为json
with open(配置文件, "r+", encoding='utf-8') as json_file:
    if os.path.getsize(配置文件):
        # 由于没有检测json的合法性可能会抛出错误
        配置信息 = json.load(json_file)


if 配置信息["游戏路径"] == "":
    '''打开选择文件夹对话框'''
    # 初始化tk
    root = tk.Tk()
    # 隐藏主窗口
    root.withdraw()
    # 打开文件对话框
    选择的文件夹 = filedialog.askdirectory(
        title='选择魔兽世界根目录如：X:\Games\World of Warcraft\\') or os.getcwd()  # 获得选择好的文件夹
    # Filepath = filedialog.askopenfilename() #获得选择好的文件
    配置信息["游戏路径"] = os.path.normcase(选择的文件夹+"\_classic_")


def 写出配置(data):
    # 写出配置
    with open(配置文件, "w", encoding='utf-8') as json_file:
        # 把dict对象转为json并允许非非ASCII字符
        json_file.write(json.dumps(data, ensure_ascii=False))


def 组合地址(版本号):
    return "http://wow.bfupdate.178.com/BigFoot/Interface/classic/Interface.%s.zip" % (版本号)


def fun(配置):
    urls = []
    版本尾 = re.match(r'.*\.(\d+)$', 配置信息["当前版本"]).group(1)

    for i in range(配置["线程"]):
        # 取最后一个递增版本号
        url = re.sub(r'\d+(?=.zip$)', str(int(版本尾)+i), 组合地址(配置信息["当前版本"]))
        # 测试访问
        r = requests.get(url, stream=True)
        响应代码 = r.status_code
        if 响应代码 == 200:
            print(url)
            urls.append(url)

    最新版本 = re.match(
        r'.*(?<=Interface\.)([\d\.]+)(?=\.zip$)', urls[-1]).group(1)

    if 配置信息["当前版本"] == 最新版本:
        ctypes.windll.user32.MessageBoxW(0, u"当前已是最新版本，无需更新。", u"小提示", 0)
        sys.exit(0)

    # 写出配置
    配置信息["当前版本"] = 最新版本
    # 并集后会打乱排列顺序 不适宜取最后的元素 因为得到的内容是错误的
    配置信息["历史"] = list(set(配置信息["历史"]) | set(urls))

    写出配置(配置信息)

    r = requests.get(组合地址(配置信息["当前版本"]), stream=True)

    响应代码 = r.status_code

    # 检查是否访问成功  响应代码, 编码方式
    # print("响应代码: %s \n编码: %s" % (r.status_code, r.encoding))
    if 响应代码 == 200:
        文件大小 = r.headers['Content-Length']
        保存路径 = os.path.normcase("%s.zip" % (配置信息["当前版本"]))
        with open(保存路径, 'wb') as fd:
            for chunk in r.iter_content(int(文件大小)):
                fd.write(chunk)

    # 解压程序
    z = zipfile.ZipFile(保存路径, "r")
    z.extractall(配置信息["游戏路径"])
    z.close()

    ctypes.windll.user32.MessageBoxW(0, u"安装完成！", u"插件进度", 0)


if __name__ == '__main__':
    写出配置(配置信息)
    fun(配置信息)
    pass
