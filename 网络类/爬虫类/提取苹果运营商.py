'''
# 2020.8.18
作者：絕版大叔、    QQ 250740270
用途: 用于从苹果提取电信运营商ipcc配置文件
'''

import asyncio
import os
import requests
from lxml import etree  # xml处理模块
import functools


async def get运营商文件(url):
    loop = asyncio.get_running_loop()
    # 获取原始响应内容  stream=True  配合 response.raw.read(size) 使用
    res = loop.run_in_executor(
        None, functools.partial(requests.get, url))
    return await res


async def main():
    # 下载苹果相关文件
    url = r"http://ax.phobos.apple.com.edgesuite.net/WebObjects/MZStore.woa/wa/com.apple.jingle.appserver.client.MZITunesClientCheck/version"
    response = await asyncio.create_task(get运营商文件(url))
    响应头 = {
        "页面大小": str(int(response.headers["content-length"])/1024/1024)+"MB",
        "请求类型": response.headers['Content-Type']
    }

    print(response.raw.read(10), 响应头)
    # txt = response.text
    name = url.rsplit("/")[-1]
    filePath = os.path.realpath(name+".xml")
    # 用文本流的方式写到文件中  大小文件通吃
    with open(filePath, mode='wb') as fd:
        # 分段读取
        for chunk in response.iter_content(chunk_size=512*100):
            fd.write(chunk)

    # 从字符串解释
    # filePath = os.path.realpath("version.xml")
    root = etree.parse(filePath).getroot()
    keys = root.xpath("/plist/dict/dict/key")

    arr = []
    for key in keys:
        if key.text == "ChinaTelecom_USIM_cn":
            # 获取下一个同胞节点
            dicts = key.getnext()
            IOS版本 = dicts.xpath("key/text()")[:-1]
            运营商版本 = dicts.xpath("dict/string[1]/text()")
            下载地址 = dicts.xpath("dict/string[2]/text()")
            for i in range(len(IOS版本)):
                arr.append(
                    {
                        "IOS版本": IOS版本[i],
                        "运营商版本": 运营商版本[i],
                        "下载地址": 下载地址[i]
                    })
    print(arr)

asyncio.run(main())
