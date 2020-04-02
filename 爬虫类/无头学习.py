# -*- coding: utf-8 -*-

'''
                        BY AIR 2020.3.27

需要用到的包
    pip install selenium -U -i https://pypi.tuna.tsinghua.edu.cn/simple         无头浏览器 官方版
    pip install selenium-wire -i https://mirrors.aliyun.com/pypi/simple/        无头浏览器 请求拦截版 可改请求头 响应数据
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



'''
import re
import json
import os
import time
import pickle
# 获取域名用
from urllib.parse import urlparse
from selenium import webdriver
# selenium扩展版
# from seleniumwire import webdriver
from browsermobproxy import Server

# 创建代理服务器
server = Server(
    r'D:\Git\tools\browsermob-proxy-2.1.4\bin\browsermob-proxy.bat')
server.start()
proxy = server.create_proxy()

# 修改当前工作目录为脚本运行目录
os.chdir(os.path.dirname(__file__))

# 浏览器相关配置
option = webdriver.ChromeOptions()


# 谷歌浏览器配置
def setChromeOption(option):
    # 不加载图片
    prefs = {"profile.managed_default_content_settings.images": 2}
    # 添加实验性质的设置参数
    # option.add_experimental_option("prefs", prefs)
    # 添加启动参数
    # option.add_argument('--headless')   # 无头模式
    # option.add_argument('--disable-gpu')
    # option.add_argument('lang=en.UTF-8')   # 设置语言
    # option.add_argument('--proxy-server=http://127.0.0.1:10000') # 设置代理
    option.add_argument("--proxy-server={0}".format(proxy.proxy))
    option.add_argument('--ignore-certificate-errors')

# 读取cookies


def loadCookies(CookiesName):
    '''
    读入cookies
    '''
    # 如果文件存在
    isFile = os.path.isfile(CookiesName)
    # 打开文件后读入cookies
    if isFile:
        with open(CookiesName, "rb") as json_file:
            return pickle.load(json_file)
    return False

# 登录并记录cookies


def loginSaveCookies(url):
    '''
    登录网站并保存cookies
    '''
    # 创建浏览器
    brower = webdriver.Chrome()
    # 登录成功后跳转的网页
    jmpurl = r'https://pc-shop.xiaoe-tech.com/appi4OKpaUS3431'
    # 打开网页
    brower.get(url)
    # 延迟处理 等待10秒
    brower.implicitly_wait(10)
    # 捕获网站标题
    name = urlparse(url).hostname
    while True:
        print("等待登录")
        # 延迟3秒
        time.sleep(3)
        # 扫码成功 判断登录成功 304跳转地址是否一样
        while brower.current_url == jmpurl:
            print("登录成功")
            # 保存 cookies
            cookies = brower.get_cookies()
            # 浏览器关闭
            brower.quit()
            # 保存到文件
            with open(name, "wb") as data:
                pickle.dump(cookies, data)
            return cookies

# 响应请求数据回调


def custom(req, req_body, res, res_body):
    path = urlparse(req.path).path
    if path == "/appi4OKpaUS3431/open/column.resourcelist.get/2.0":
        req_body = bytes(str(req_body, "utf-8").replace("page_size%5D=10",
                                                        "page_size%5D=20"), encoding="utf8")
        req_body = b""
    pass


def 爬取(url, cookies):

    # 永不超时，获取所有请求
    # opt = {"connection_timeout": None, "ignore_http_methods": [],
    #        'custom_response_handler': custom}
    # 捕获请求和响应
    # opt = {'custom_response_handler': custom}

    # 修改谷歌配置
    setChromeOption(option)

    # 创建浏览器
    # driver = webdriver.Chrome(chrome_options=option, seleniumwire_options=opt)
    driver = webdriver.Chrome(chrome_options=option)

    # 捕获特定请求
    # driver.scopes = [
    #     '.*/appi4OKpaUS3431/open/.*'
    # ]

    proxy.headers({"cookies": "{}={}".format(
        cookies[0]['name'], cookies[0]['value'])})

    # 开启代理监控
    # 开启代理监控，如果不监控会拿不到请求内容
    # 捕获 头 、内容主体、二进制数据
    proxy.new_har("login", options={
                  'captureContent': True, 'captureHeaders': True, 'captureBinaryContent': True})
    # proxy.har
    # 访问页面
    driver.get(url)
    # 使用 cookies
    # for cookie in cookies:
    #     # obj = {k: v for k, v in cookieObj.items() if re.match(r'^value$|^name$', k)}
    #     # 获取 cookies 对象中的包含 var、name的键值
    #     driver.add_cookie(
    #         {"value": cookie['value'], "name": cookie['name']})

    driver.implicitly_wait(10)
    # 使用 cookies 后需要重新访问页面
    driver.get(url)

    # 延迟处理 等待10秒
    driver.implicitly_wait(10)

    driver.back()

    # 如果没跳转成功 则表示 cookies 失效
    # if not urlparse(driver.current_url).path == urlparse(url).path:
    #     # 关闭浏览
    #     driver.quit()
    #     # 重新获取 cookies 并重启本程序
    #     Cookies = loginSaveCookies(url)
    #     爬取(url, Cookies)
    #     return

    # ajax = []
    # 等待响应返回
    # request = driver.wait_for_request('/appi4OKpaUS3431/open/combine/1.0')
    # 返回的二进制响应数据转为str再转为json
    # request = json.loads(str(request.response.body, "utf-8"))
    # print(request)

    # https: // pc-shop.xiaoe-tech.com/appi4OKpaUS3431/columnist_detail?id = p_5bb04719e2a39_1B6l08K9

    # 获取视频接口
    # https://pc-shop.xiaoe-tech.com/appi4OKpaUS3431/open/video.detail.get/1.0
    # post
    # data%5Bresource_id%5D=v_5b8e33216acdf_68kY3tpB

    # 获取ID
    # https://pc-shop.xiaoe-tech.com/appi4OKpaUS3431/open/column.resourcelist.get/2.0

    # for request in driver.requests:
    #     # 捕获所有 post 发送请求 和 已经响应了的请求
    #     if request.method == "POST":
    #         print(request.response)
    #         # ajax.append(request)
    #     # print(
    #     #     1111,
    #     #     request.path,
    #     #     request.response.status_code,
    #     #     request.response.headers['Content-Type']
    #     # )

    # print(ajax)
    # $$('.columnist-item a')
    # 执行控制台命令
    # driver.execute_script(拦截ajax)
    # 找到所有课程

    # ids = []
    # # 获取课程的数量
    # els = len(driver.find_elements_by_css_selector("div.contentMain"))
    # for i in range(els):
    #     # 获取课程节点
    #     node = driver.find_elements_by_css_selector("div.contentMain")[i]
    #     if not node:
    #         # driver.quit()
    #         return False
    #     # 删除旧的请求
    #     del driver.requests
    #     node.click()

    # driver.execute_script()

    # 捕获所有 post 发送请求 和 已经响应了的请求
    # isfai = True
    # while isfai:
    #     driver.implicitly_wait(10)
    #     for request in driver.requests:
    #         path = urlparse(request.path).path
    #         if path == "/appi4OKpaUS3431/open/column.resourcelist.get/2.0":
    #             # request.body = bytes(
    #             #     str(request.body, "utf-8").replace("page_size%5D=10", "page_size%5D=100"), encoding="utf8")
    #             print('\n============', path, '=================\n')
    #             isfai = False
    #             break

    # 获取请求头判断是否ajax请求 判断字典是否存在key
    # if ('x-requested-with' in request.headers) or (request.method == "POST"):
    # if request.method == "POST":
    #     print('\n====', request.path, '====\n')
    #     # ajax.append(request)
    #     print(request)
    # if urlparse(request.path).path == '/appi4OKpaUS3431/open/column.resourcelist.get/2.0':

    # request = driver.wait_for_request(
    # '/appi4OKpaUS3431/open/column.resourcelist.get/2.0')
    # driver.wait_for_request(
    #     '/appi4OKpaUS3431/open/column.resourcelist.get/2.0')
    # # 返回的二进制响应数据转为str再转为json
    # request = json.loads(str(request.response.body, "utf-8"))
    # # # 保存捕获的id
    # for data in request['data']:
    #     ids.append((data['title'], data['id']))

    # print(ids)

    # 打开其中一个课程
    #
    # # 找到课程栏目
    # node = driver.find_elements_by_class_name("div.columnist-item")
    # # 点开第一个
    # node[0].click()


if __name__ == "__main__":

    # 源
    url = r'https://pc-shop.xiaoe-tech.com/appi4OKpaUS3431'

    # 取域名
    # domian = re.match(r".*//(.*)/", url).group(1)
    hostname = urlparse(url).hostname

    # # 判断当前页面跳到了登录页面 表示 cookies 失效
    # if urlparse(brower.current_url).path == r"/appi4OKpaUS3431/login":
    #     return False

    # 读入 cookies 不存在则 重新登录获取
    Cookies = loadCookies(hostname) or loginSaveCookies(url)

    # domian["Cookies"] = Cookies

    # 如果 cookies 不存在
    if not Cookies:
        print("未找到cookies")
        exit()

    爬取(url, Cookies)
