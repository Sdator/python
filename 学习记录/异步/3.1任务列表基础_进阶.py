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


async def 任务列表方法1():
    print(1)
    # 创建任务列表
    tasks = [
        asyncio.create_task(demo()),
        asyncio.create_task(demo2())
    ]

    # 返回结果和运行状态  一般用作返回给外部处理结果
    done, pending = await asyncio.wait(tasks)
    print(done)
    # 这种方式任务会提前完成返回结果 无序的
    for res in done:
        print(await res)


async def 任务列表方法2():
    print(1)
    # 创建任务列表
    tasks = [
        asyncio.create_task(demo()),
        asyncio.create_task(demo2())
    ]

    # 等待列表 这种方式任务会提前完成返回结果 无序的 适合运行没有依赖的任务列表
    for task in asyncio.as_completed(tasks):
        # 获取返回结果
        data = await task
        print(data, type(data))


async def 任务列表方法3():
    print(1)
    # 创建任务列表
    tasks = [
        asyncio.create_task(demo()),
        asyncio.create_task(demo2())
    ]
    # 等待列表 会按照任务顺序返回结果 有序的
    tasks = await asyncio.gather(*tasks)
    for v in tasks:
        print(v, type(v))


# 推荐使用的一种精简方法
async def 任务列表方法4():
    print(1)
    # 创建任务列表
    tasks = [
        demo(),
        demo2()
    ]
    # 等待列表 会按照任务顺序返回结果 有序的
    tasks = await asyncio.gather(*tasks)
    for v in tasks:
        print(v, type(v))


old = now()
# asyncio.run(任务列表方法1())
# asyncio.run(任务列表方法2())
# asyncio.run(任务列表方法3())
asyncio.run(任务列表方法4())
print("耗时：{:.2f}秒".format(now() - old))
