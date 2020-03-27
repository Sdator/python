# -*- coding: utf-8 -*-

'''
                        BY AIR 2020.3.27

需要用到的包
    pip install selenium -U -i https://pypi.tuna.tsinghua.edu.cn/simple
    -i      使用指定源
    -U      升级到最新版
    --user  将Python 程序包安装到 $HOME/.local 路径下 其中包含三个字文件夹：bin，lib 和 share

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


import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# 修改当前工作目录为脚本运行目录
os.chdir(os.path.dirname(__file__))


# 浏览器参数设置 设置为无头隐藏 关闭gpu渲染
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# driver = webdriver.Chrome(chrome_options=chrome_options)
option = webdriver.ChromeOptions()
# option.add_argument('--proxy-server=http://127.0.0.1:10000')

# 创建驱动对象
driver = webdriver.Chrome(options=option)
# 延迟处理 等待10秒
driver.implicitly_wait(10)

# driver.get("http://pc-shop.xiaoe-tech.com/appi4OKpaUS3431")
driver.get("http://www.kpcb.org.cn/h-nd-342.html#_np=111_330")

node = driver.find_elements_by_tag_name("p a")

for el in node:
    if el.text == "点我进入":
        el.click()
pass

# if __name__ == "__main__":
#     pass
#     # driver.get("https://cnblogs.com/")
#

# driver.get("https://www.pornhub.com/")
