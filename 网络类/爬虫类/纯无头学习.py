# -*- coding: utf-8 -*-

'''
                        BY AIR 2020.3.27

需要用到的包
    pip install selenium -U -i https://pypi.tuna.tsinghua.edu.cn/simple         无头浏览器 官方版
    pip install selenium-wire -i https://mirrors.aliyun.com/pypi/simple/        无头浏览器 数据拦截 可改请求头 响应数据
    pip install mitmproxy -i https://pypi.tuna.tsinghua.edu.cn/simple          中间人代理 拦截请求响应修改用
    -i      使用指定源
    -U      升级到最新版
    --user  将Python 程序包安装到 $HOME/.local 路径下 其中包含三个字文件夹：bin，lib 和 share

    虚拟环境
    pip install pipx


参考连接
    http://www.python3.vip/doc/tutorial/selenium/01/
    https://sites.google.com/a/chromium.org/chromedriver/downloads


    //查找所有包含'撤下'的元素
    Array.from(
    document.querySelectorAll(".item_market_action_button_contents")
    ).filter(el => el.innerText === '撤下');

    //查找第一个包含'撤下'的元素
    Array.from(
    document.querySelectorAll(".item_market_action_button_contents")
    ).find(el => el.innerText === '撤下');

    # 重新生成pip
python -m ensurepip
# 更新pip
python -m pip install --upgrade -i https://pypi.tuna.tsinghua.edu.cn/simple pip

pip install -U autopep8 --user -i https://pypi.tuna.tsinghua.edu.cn/simple


弃坑
    使用了 selenium 和 selenium-wire 均无法解决
    学习 browsermobproxy 中间代理碰到一些问题


    selenium-wire
        偏向捕获请求和响应 但无法修改请求body 可修改响应body
        采用了时间记录捕获帧
        使用回调函数 捕获数据 custom(req, req_body, res, res_body):


'''
import re
import json
import os
import time
import pickle
# 获取域名用
from urllib.parse import urlparse
from selenium import webdriver
import requests
import asyncio

# 修改当前工作目录为脚本运行目录
os.chdir(os.path.dirname(__file__))

# 浏览器相关配置
option = webdriver.ChromeOptions()

Cookies = None

# 谷歌浏览器配置


def setChromeOption(option):
    # 不加载图片
    # prefs = {"profile.managed_default_content_settings.images": 2}
    # 添加实验性质的设置参数
    # option.add_experimental_option("prefs", prefs)
    # 添加启动参数
    # option.add_argument('--headless')   # 无头模式
    # option.add_argument('--disable-gpu')# 禁用GPU加速
    option.add_argument('lang=en.UTF-8')   # 设置语言
    # option.add_argument('--proxy-server=http://127.0.0.1:10000') # 设置代理
    # option.add_argument("--proxy-server={0}".format(proxy.proxy))
    # option.add_argument('--ignore-certificate-errors')# 禁用扩展插件并实现窗口最大化
    pass


async def 延迟():
    await asyncio.sleep(1)


def 爬取(url):
    # 修改谷歌配置
    setChromeOption(option)
    # 创建浏览器
    driver = webdriver.Chrome(chrome_options=option)
    driver.get(url)
    driver.implicitly_wait(10)
    driver.close()


async def main():
    # 源
    # url = r'https://pc-shop.xiaoe-tech.com/appi4OKpaUS3431'
    url = r"https://study.163.com/course/introduction.htm?courseId=1512007#/courseDetail?tab=1"
    爬取(url)
    print(222222)
    # while True:
    #     await 延迟()
    #     print(111)


asyncio.run(main())
