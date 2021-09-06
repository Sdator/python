import asyncio
import time


def now():
    return time.time()


async def demo():
    print(2)
    await asyncio.sleep(2)
    print(5)
    return 123


async def demo2():
    print(3)
    await asyncio.sleep(1)
    print(4, "我比你执行快")
    return 456


# 一般不会用这种写法 除非任务极少
async def main():
    print(1)
    # 创建任务
    task1 = asyncio.create_task(demo())
    task2 = asyncio.create_task(demo2())

    # IO等待
    res1 = await task1
    res2 = await task2
    print(res1, res2)


# 一般不会用这种写法 除非任务极少
async def 简写方法():
    print(1)

    # # 创建任务
    # task1 = demo()
    # task2 = demo2()

    # IO等待
    # res1 = await task1
    # res2 = await task2

    # 实际上可以直接写 等同上面
    res1 = await demo()
    res2 = await demo2()

    print(res1, res2)


old = now()
# asyncio.run(main())
asyncio.run(简写方法())
print("耗时：{:.2f}秒".format(now() - old))
