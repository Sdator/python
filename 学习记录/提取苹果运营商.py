

import asyncio
import os
import requests
from lxml import etree  # xml处理模块


async def get运营商文件(url):
    loop = asyncio.get_running_loop()
    res = loop.run_in_executor(None, requests.get, url)
    return await res


async def main():
    # 下载苹果相关文件
    # url = r"http://ax.phobos.apple.com.edgesuite.net/WebObjects/MZStore.woa/wa/com.apple.jingle.appserver.client.MZITunesClientCheck/version"
    # response = await asyncio.create_task(get运营商文件(url))
    # txt = response.text
    # name = url.rsplit("/")[-1]
    # fileName = os.path.realpath(name)
    # with open(fileName, mode='w') as file_object:
    #     file_object.write(txt)

    # # 从字符串解释
    # node = dom.parseString(txt)
    filePath = os.path.realpath("version.xml")
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
            i = 0
            for v in IOS版本:
                arr.append(
                    {
                        "IOS版本": IOS版本[i],
                        "运营商版本": 运营商版本[i],
                        "下载地址": 下载地址[i]
                    })
                i += 1
    print(arr)

    # for v in dicts:
    #     print(v.text)


asyncio.run(main())
