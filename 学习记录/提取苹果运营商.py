

import asyncio
import os
import requests
import xml.dom.minidom as dom  # xml处理模块


async def get运营商文件(url):
    loop = asyncio.get_running_loop()
    res = loop.run_in_executor(None, requests.get, url)
    return await res


async def main():
    url = r"http://ax.phobos.apple.com.edgesuite.net/WebObjects/MZStore.woa/wa/com.apple.jingle.appserver.client.MZITunesClientCheck/version"
    response = await asyncio.create_task(get运营商文件(url))
    name = url.rsplit("/")[-1]
    fileName = os.path.realpath(name)
    with open(fileName, mode='w') as file_object:
        file_object.write(response.text)
        # print(111)
        print(response, 44444)

asyncio.run(main())
