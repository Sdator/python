import asyncio
import requests
import functools


async def fetch(url):
    # 把其他函数利用 functools.partial 生成异步函数
    future = asyncio.get_event_loop().run_in_executor(
        None, functools.partial(requests.get, url))
    return future


def main():
    """
    读取地址
    """
    url = "https://api.cloudflare.com/client/v4/ips"
    get = fetch(url)

    abc = asyncio.run(get)

    print(abc, 22222, 444444444444)


if __name__ == '__main__':
    main()
