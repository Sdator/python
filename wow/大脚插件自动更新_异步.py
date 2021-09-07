# -*- coding: utf-8 -*-
'''
by 绝 2019.10.6  QQ 250740270

本程序用于自动更新大脚插件

用到的包
    conda install pyinstaller -y    # 打包exe
    conda install aiohttp -y        # 异步http
    conda install requests          # 网络通信

    conda install --name wow flake8 -y # 代码检测

生成二进制文件

    -F 表示生成单个可执行文件
    -w 表示去掉控制台窗口，这在GUI界面时非常有用。不过如果是命令行程序的话那就把这个选项删除吧！
    -i 表示可执行文件的图标

    pyinstaller -F -w 大脚插件自动更新.py -i wow.ico

导出当前环境
conda env export > py3_pack.yaml

导入环境
conda env create -f py3_pack.yaml

'''


import json
import sys
import os
import re                       # 正则
import zipfile                  # 解包
import tkinter as tk            # 组件
from tkinter import filedialog  # 选择框
import tkinter.messagebox       # 消息框
import ctypes  # 弹窗
from functools import reduce
import time
import asyncio  # 异步
import aiohttp


client = aiohttp.ClientSession()

# 引用类型可以直接被函数读取并修改
配置信息 = dict()
配置文件 = "config.json"

预设配置信息 = {
    "游戏路径": "",
    "当前版本": "1.13.2.18",
    "最新版本": "1.13.2.18",
    # "当前版本": "2.5.2.99",
    "线程": 10,
    "历史": ['http://wow.bfupdate.178.com/BigFoot/Interface/classic/Interface.1.13.2.18.zip', ]
}

# 获取当前脚本路径
# path1 = sys.path[0]


def now():
    return time.time()


def 组合地址(版本号):
    return "http://wow.bfupdate.178.com/BigFoot/Interface/classic/Interface.%s.zip" % (版本号)


def 选择游戏目录():
    # 判断key是否存在的正规写法
    # 如果配置中不存在路径则触发路径选择
    if not('游戏路径' in 配置信息) or not(os.path.exists(os.path.dirname(配置信息["游戏路径"]))):
        '''打开选择文件夹对话框'''
        # 初始化tk
        root = tk.Tk()
        # 隐藏主窗口
        root.withdraw()
        # 打开文件对话框
        选择的文件夹 = filedialog.askdirectory(
            title=r'选择魔兽世界根目录如：X: \Games\World of Warcraft') or os.getcwd()
        # 获得选择的文件
        # Filepath = filedialog.askopenfilename()
        # 检测选择目录
        if sys.path[0] == 选择的文件夹:
            if msg("提示", f"检测到选择目录和当前目录相同，是否要下载到当前目录？\n选择目录为：{选择的文件夹}", 0x1) == 2:
                exit()

        # 获得选择的文件夹
        配置信息["游戏路径"] = os.path.normcase(选择的文件夹 + "\\_classic_")


def 读入配置(path):

    # 路径合法性
    配置文件 = os.path.normcase(path)

    # 文件不存在创建
    if not os.path.isfile(配置文件):
        print("文件不存在")
        # 返回空配置
        return 预设配置信息

    # 读入配置
    # 以utf8打开文件 并转为json
    with open(配置文件, "r+", encoding='utf-8') as json_file:
        # 检测json的合法性
        try:
            config = json.load(json_file)
            # 如果是字典类型才是正确的
            if type(config) == dict:
                return config
            print("json解析错误 使用预设配置")
            return 预设配置信息
        except json.decoder.JSONDecodeError as e:
            print("json解析失败 使用预设配置,错误信息：", e)
            return 预设配置信息


def 写出配置(data):
    # 覆盖原有
    with open(配置文件, "w", encoding='utf-8') as json_file:
        # 把dict对象转为json并允许非ASCII字符
        json_file.write(json.dumps(data, ensure_ascii=False))


def msg(标题, 内容, *t):
    # MB_OK = 0x0
    # MB_OKCXL = 0x01
    # MB_YESNOCXL = 0x03
    # MB_YESNO = 0x04
    # MB_HELP = 0x4000
    # ICON_EXLAIM = 0x30
    # ICON_INFO = 0x40
    # ICON_STOP = 0x10
    # WS_EX_TOPMOST = 0x40000
    MB_SYSTEMMODAL = 0x1000
    MB = 0
    if(t != ()):
        # 传入的样式进行或处理
        MB = reduce(lambda x, y: x | y, t)
    return ctypes.windll.user32.MessageBoxW(
        0, 内容, 标题, MB_SYSTEMMODAL | MB)


async def fetch(session, url):
    async with session.head(url) as resp:
        if resp.status == 200:
            # print(url, resp.headers)
            # print(await resp.text())
            # assert resp.status == 200
            # return resp.status
            return url


async def 获取最新版本(client):
    old = now()

    # 版本号 分割 并转为整数
    a, b, c, d = [int(i) for i in 配置信息["当前版本"].split(".")]
    # 上一个响应 = None
    # 使用会话
    async with aiohttp.ClientSession() as session:
        # 创建异步任务列表
        tasks = [fetch(session, 组合地址(f'{a}.{b}.{c}.{d+i}'))
                 for i in range(配置信息["线程"])]
        # 异步访问
        urls = await asyncio.gather(*tasks)
        # 去除 None 结果
        历史 = [url for url in urls if url]

        print("获取版本耗时：{:.2f}秒".format(now() - old))

        if not len(历史):
            print("找不到可用的版本，尝试加大线程数量或直接修改配置“当前版本”为最近的一个版本的近似数")
            msg(u"错误", u"找不到可用的版本，尝试加大线程数量或直接修改配置“当前版本”为最近的一个版本的近似数。")
            # sys.exit(0)
            return

        # 正则匹配出版本号
        最新版本 = re.match(r'.*(\d+\.\d+\.\d+\.\d+)', 历史[-1]).group(1)
        # 历史版本合并 去重复 排列
        配置信息["历史"] = sorted(set(配置信息["历史"] + 历史))

        if 配置信息["当前版本"] == 最新版本:
            msg(u"提示", u"当前已是最新版本，无需更新")
            # sys.exit(0)
            return

        配置信息["最新版本"] = 最新版本

        return 历史[-1]


async def 下载插件(client, url):
    old = now()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            文件大小 = int(resp.headers['Content-Length'])
            保存路径 = os.path.normcase("%s.zip" % (配置信息["最新版本"]))
            with open(保存路径, 'wb') as fd:
                while True:
                    chunk = await resp.content.read(文件大小)
                    if not chunk:
                        print("下载耗时：{:.2f}秒".format(now() - old))
                        return 保存路径
                    fd.write(chunk)


# 解压程序
def 解压(file, path):
    # 打开压缩包
    z = zipfile.ZipFile(file, "r")
    # 解压到指定位置
    z.extractall(path)
    z.close()
    msg(u"提示", u"安装完成！")


def 打开文件夹(paht):
    if os.path.exists(paht):
        os.system("start " + paht)
    else:
        msg("找不到目录", "压缩包存在问题或解压失败")


async def main(client=123):
    # 更新全局变量的值 由于无法直接赋值但可以使用对象方法
    配置信息.update(读入配置(配置文件))
    选择游戏目录()
    url = await 获取最新版本(client)
    if url:
        name = await 下载插件(client, url)
        解压(name, 配置信息["游戏路径"])
        打开文件夹(配置信息["游戏路径"])

    写出配置(配置信息)


if __name__ == '__main__':
    # 错误处理
    try:
        asyncio.run(main())
        # asyncio.run(client.close())  # 关闭会话客户端

        # asyncio.get_event_loop().run_until_complete(main(client))
        # loop = asyncio.get_event_loop()
        # client = aiohttp.ClientSession()
        # results = loop.run_until_complete(main(client))
        # 要手动关闭自己创建的ClientSession，并且client.close()是个协程，得用事件循环关闭
        # loop.run_until_complete(client.close())
        # # 在关闭loop之前要给aiohttp一点时间关闭ClientSession
        # loop.run_until_complete(asyncio.sleep(3))
        # loop.close()
        # print(results)
        # print(type(results))

    except json.decoder.JSONDecodeError as e:
        # 配置信息 = 预设配置信息
        print('解析json失败，使用预设配置，错误:', e)
