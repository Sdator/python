import asyncio
import time


def now():
    return time.time()


async def demo():
    print(2)
    await asyncio.sleep(2)  # 模拟 IO 操作 等待2秒
    print(3)
    return 132


async def main():
    print(1)
    # 调用其他异步函数 等待返回结果
    data = await demo()
    print(data)


old = now()
asyncio.run(main())
print("耗时：{:.2f}秒".format(now() - old))
