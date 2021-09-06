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


# 简写方式可以直接把任务列表写到外面
任务集 = [
    main(),
    demo()
]


old = now()
asyncio.run(asyncio.wait(任务集))  # py3.7的新写法
print("耗时：{:.2f}秒".format(now() - old))
