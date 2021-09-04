# -*- coding: utf-8 -*-
'''
by 绝 2019.10.6  QQ 250740270

本程序用于自动更新大脚插件

用到的包
conda install pyinstaller   # 打包exe
conda install requests      # 网络通信

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

# 网页
import requests
import json
import sys
import os
import re                       # 正则
import zipfile                  # 解包
import tkinter as tk            # 组件
from tkinter import filedialog
import tkinter.messagebox       # 消息框

# 弹窗
import ctypes


configFile = "config.json"
# 配置文件 = os.path.normcase(configFile)


预设配置信息 = {
    "游戏路径": "",
    "当前版本": "2.5.2.101",
    "线程": 10,
    "历史": ['http://wow.bfupdate.178.com/BigFoot/Interface/classic/Interface.1.13.2.18.zip', ]
}
# 引用类型可以直接被函数读取并修改
配置信息 = dict()

# 获取当前脚本路径
# path1 = sys.path[0]


def 组合地址(版本号):
    return "http://wow.bfupdate.178.com/BigFoot/Interface/classic/Interface.%s.zip" % (版本号)


def 选择游戏目录():
    # 检测路径是否存在
    if not os.path.exists(配置信息["游戏路径"]):
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
        # 空文件检测
        # if os.path.getsize(配置文件):
        # 由于没有检测json的合法性可能会抛出错误
        try:
            config = json.load(json_file)
            # 如果是字典类型才是正确的
            if type(config) == dict:
                return config
            print("json解析错误 使用预设配置")
            return 预设配置信息
        except json.decoder.JSONDecodeError as e:
            print("json解析失败 使用预设配置")
            return 预设配置信息


def 写出配置(data):
    # 覆盖原有
    with open(configFile, "w", encoding='utf-8') as json_file:
        # 把dict对象转为json并允许非ASCII字符
        json_file.write(json.dumps(data, ensure_ascii=False))


def 获取插件(配置):
    # 历史版本
    urls = []
    版本尾 = re.match(r'.*\.(\d+)$', 配置信息["当前版本"]).group(1)

    for i in range(配置["线程"]):
        # 取最后一个递增版本号
        url = re.sub(r'\d+(?=.zip$)', str(int(版本尾)+i), 组合地址(配置信息["当前版本"]))
        # 测试访问
        r = requests.get(url, stream=True)
        响应代码 = r.status_code
        # 如果有响应就添加到数组
        if 响应代码 == 200:
            print(url)
            urls.append(url)

    最新版本 = re.match(
        r'.*(?<=Interface\.)([\d\.]+)(?=\.zip$)', urls[-1]).group(1)

    if 配置信息["当前版本"] == 最新版本:
        ctypes.windll.user32.MessageBoxW(0, u"当前已是最新版本，无需更新。", u"小提示", 0)
        sys.exit(0)

    # 更新配置
    配置信息["当前版本"] = 最新版本
    # 并集后会打乱排列顺序 不适宜取最后的元素 因为得到的内容是错误的
    配置信息["历史"] = list(set(配置信息["历史"]) | set(urls))

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


def 打开文件夹():
    os.system("start "+配置信息["游戏路径"])


def main():
    # 更新全局变量的值 由于无法直接赋值但可以使用对象方法
    配置信息.update(读入配置(configFile))
    选择游戏目录()
    获取插件(配置信息)
    写出配置(配置信息)
    打开文件夹()
    pass


if __name__ == '__main__':
    # 错误处理
    try:
        main()
    except json.decoder.JSONDecodeError as e:
        # 配置信息 = 预设配置信息
        print('解析json失败，使用预设配置，错误:', e)
