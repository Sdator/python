import asyncio
import aiohttp
import time

from aiohttp import ClientSession


def now():
    return time.time()


async def hello(session, url):
    async with session.get(url) as response:
        # assert response.status == 200
        # 读取文本
        # print(await response.text())
        print(response)
        # 读取二进制数据
        # response = await response.read()
        # print(response)


async def main():
    # 使用连接池请求
    async with ClientSession() as session:
        tasks = [f"https://www.baidud.com/{item}" for item in range(100)]

        # url = "https://www.baidud.com/"
        # data = await hello(session, url)
        print(tasks)


old = now()

try:
    # asyncio.run(main())  # 携程对象可以直接运行 但是会报错 这里使用传统模式
    asyncio.get_event_loop().run_until_complete(main())
except aiohttp.client_exceptions.ClientConnectorError as e:
    print("远程计算机拒绝网络连接:", e)
except AssertionError as e:
    print("网络状态非200", e)


print("耗时：{:.2f}秒".format(now() - old))
