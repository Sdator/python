# -*- coding: utf-8 -*-
'''
by 绝 2019.10.6  QQ 250740270

本程序用于自动更新大脚插件

用到的第三方包
    pyinstaller # 打包exe
    aiohttp     # 异步http通信
    conda install --name wow aiohttp pyinstaller -y # 安装到wow环境中

生成二进制文件

    -F 表示生成单个可执行文件
    -w 表示去掉控制台窗口，这在GUI界面时非常有用。不过如果是命令行程序的话那就把这个选项删除吧！
    -i 表示可执行文件的图标

    pyinstaller -F -w 大脚插件自动更新_异步.py -i wow.ico

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
import ctypes  # 弹窗 打包不需要🙅‍
from functools import reduce  # 打包不需要🙅‍
import time  # 测试用打包不需要🙅‍
import asyncio  # 异步
import aiohttp

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


# 修改当前工作目录为脚本运行目录
# 打包之前要把这个注释掉 否则会报错 路径不合法 可能是使用了中文的问题
# os.chdir(os.path.dirname(__file__))


# 界面交互
class WindowGUI():
    __root = tk.Tk()
    __root.withdraw()  # 隐藏Tk窗口
    __root.attributes("-topmost", True)

    # 信息框

    @staticmethod
    def msg(title, msg, type=0):
        # 为了兼容之前的代码 做一个返回值转换
        isOK = True if tk.messagebox.askquestion(
            title, msg) == "yes" else False
        return isOK

    @staticmethod
    def exit(title, msg,):
        tk.messagebox.showinfo(title, msg)
        exit()

    @staticmethod
    def 选择框(title, **args):
        选择的文件夹 = filedialog.askdirectory(
            title=title, **args)
        if not 选择的文件夹:
            defpath = os.getcwd()
            if WindowGUI.msg("提示", f"没有选择目录是否才用当前目录？\n当前目录为：{defpath}"):
                return defpath
            else:
                WindowGUI.exit("再见", "等想好了目录再来找我吧！")

        if sys.path[0] == 选择的文件夹:
            if not WindowGUI.msg("提示", f"检测到选择目录和当前目录相同，是否要下载到当前目录？\n选择目录为：{选择的文件夹}"):
                WindowGUI.exit("再见", "等想好了目录再来找我吧！")
        return 选择的文件夹

    # !调用 w32api 的信息窗口 不利于跨平台 弃用 打包不需要🙅‍
    @staticmethod
    def __msg(标题, 内容, *t):
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


# 当前时间
def now():
    return time.time()


def 组合地址(版本号):
    return "http://wow.bfupdate.178.com/BigFoot/Interface/classic/Interface.%s.zip" % (版本号)


def 选择游戏目录():
    # 判断key是否存在的正规写法
    # 如果配置中不存在路径则触发路径选择
    if not('游戏路径' in 配置信息) or not(os.path.exists(os.path.dirname(配置信息["游戏路径"]))):
        '''打开选择文件夹对话框'''
        选择的文件夹 = WindowGUI.选择框(r'选择魔兽世界根目录如：X: \Games\World of Warcraft')
        # 获得选择的文件夹
        配置信息["游戏路径"] = os.path.normcase(选择的文件夹 + "\\_classic_")


def 读入配置(path):
    # 路径合法性
    配置文件 = os.path.normcase(path)
    # 文件不存在采用预设配置
    if not os.path.isfile(配置文件):
        print("文件不存在返回预设配置")
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


async def fetch(session, url):
    async with session.head(url) as resp:
        if resp.status == 200:
            return url


async def 获取最新版本():
    old = now()
    # 版本号 分割 并转为整数
    a, b, c, d = [int(i) for i in 配置信息["当前版本"].split(".")]

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
            WindowGUI.msg(
                u"错误", u"找不到可用的版本，尝试加大线程数量或直接修改配置“当前版本”为最近的一个版本的近似数。")
            return

        # 正则匹配出版本号
        最新版本 = re.match(r'.*(\d+\.\d+\.\d+\.\d+)', 历史[-1]).group(1)
        # 历史版本合并 去重复 排列
        配置信息["历史"] = sorted(set(配置信息["历史"] + 历史))

        if 配置信息["当前版本"] == 最新版本:
            WindowGUI.msg(u"提示", u"当前已是最新版本，无需更新")
            return

        配置信息["最新版本"] = 最新版本

        return 历史[-1]


async def 下载插件(url):
    old = now()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            文件大小 = int(resp.headers['Content-Length'])
            保存路径 = os.path.normcase("%s.zip" % (配置信息["最新版本"]))
            with open(保存路径, 'wb') as fd:
                while True:
                    # 读取文件流
                    chunk = await resp.content.read(文件大小)
                    if not chunk:
                        print("下载耗时：{:.2f}秒".format(now() - old))
                        return 保存路径
                    fd.write(chunk)


def 打开文件夹(paht):
    if os.path.exists(paht):
        os.system("start " + paht)
    else:
        WindowGUI.exit("找不到目录", "压缩包存在问题或解压失败")


# 解压程序
def 解压(file, path):
    try:
        # 打开压缩包
        z = zipfile.ZipFile(file, "r")
        # 解压到指定位置
        z.extractall(path)
        z.close()
        isOpen = WindowGUI.msg(u"提示", u"安装完成！ 是否打开文件夹？")
        if isOpen:
            打开文件夹(path)
    except FileNotFoundError as e:
        print("解压失败找不到文件:", e)
        WindowGUI.exit(u"错误", u"找不到压缩文件，检测路径或文件名是否正确")
    except zipfile.BadZipFile as e:
        print("文件格式错误:", e)
        WindowGUI.exit(u"错误", u"文件格式错误,检测是否正确的zip文件")


async def main():
    # 更新全局变量的值 由于全局变量无法直接赋值 但可以执行其方法 引用类型的元素可以赋值
    配置信息.update(读入配置(配置文件))
    选择游戏目录()
    url = await 获取最新版本()
    if url:
        name = await 下载插件(url)
        # 解压(name, 配置信息["游戏路径"])
        print(url, name, 555555555)

    写出配置(配置信息)


if __name__ == '__main__':
    # 错误处理
    try:
        asyncio.run(main())
    except aiohttp.client_exceptions.ClientConnectorError as e:
        print("远程计算机拒绝网络连接:", e)
    except aiohttp.client_exceptions.InvalidURL as e:
        print("地址格式格式有误", e)
    except AssertionError as e:
        print("网络状态非200", e)
