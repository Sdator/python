import asyncio
import time

# 取当前时间


def now():
    return time.time()


async def main():
    print(1)  # 1
    # 模拟 IO 操作 等待2秒
    await asyncio.sleep(2)
    print(2)  # 4


async def demo():
    print(3)  # 2
    # 模拟 IO 操作 等待1秒
    await asyncio.sleep(1)
    print(4)  # 3


if __name__ == '__main__':
    old = now()
    # 把需要异步的函数包装到一起
    任务集 = [
        main(),
        demo()
    ]

    asyncio.run(任务集)

    print("耗时：{:.2f}秒".format(now() - old))
