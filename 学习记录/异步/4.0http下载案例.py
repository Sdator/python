import asyncio
import aiohttp
import time


def now():
    return time.time()


async def fecth(session, url):
    async with session.head(url) as response:
        # assert response.status == 200
        # 读取文本
        # print(await response.text())
        print(response.status)
        # 读取二进制数据
        # response = await response.read()
        # print(response)


async def main():
    # 在异步函数中创建
    client = aiohttp.ClientSession()
    # 使用连接池请求
    # async with ClientSession() as session:
    await fecth(client, "http://www.baidu.com")
    await fecth(client, "http://www.4399.com")


old = now()

try:
    asyncio.run(main())  # 携程对象可以直接运行 但是会报错 这里使用传统模式
    # asyncio.get_event_loop().run_until_complete(main())
except aiohttp.client_exceptions.ClientConnectorError as e:
    print("远程计算机拒绝网络连接:", e)
except AssertionError as e:
    print("网络状态非200", e)
except aiohttp.client_exceptions.InvalidURL as e:
    print("地址格式格式有误", e)

print("耗时：{:.2f}秒".format(now() - old))
