import sys
import time
import asyncio
import requests
import functools


# 取当前时间
def now(): return time.time()

# 测试


async def test2():
    return 123


async def fetch(url):
    # 把其他函数利用 functools.partial 生成异步函数
    future = asyncio.get_event_loop().run_in_executor(
        None, functools.partial(requests.get, url))

    # for v in asyncio.as_completed(tasks):
    #     b = await v
    #     print(b)
    # print(a, type(a), 4444444444444)
    # <class 'requests.models.Response'>
    # <class '_asyncio.Future'>
    return future


async def test(i=1):
    # 等待一秒
    # time.sleep(1)
    await asyncio.sleep(i)
    # asyncio.ensure_future(test(1))

    # print(a, type(a))    # <coroutine object testa at 0x000002221B9CA0C8> <class 'coroutine'>  异步对象

    # <Task pending coro=<testa() running at d:\...\异步.py:22>> <class '_asyncio.Task'>
    # print(b, type(b))

    # for v in asyncio.as_completed(b):
    #     b = await v
    #     # <coroutine object as_completed.<locals>._wait_for_one at 0x000001551E4FB248> <class 'coroutine'>
    #     print(v, type(v))
    #     print(b, type(b))
    # for v in asyncio.as_completed(testa()):
    #     print(v)
    # Traceback (most recent call last):
    # print(a, type(a), 555555555)
    # print(b, type(b), 555555555)
    # <generator object as_completed at 0x0000021D5F7BB1C8> <class 'generator'>
    # <_GatheringFuture pending> <class 'asyncio.tasks._GatheringFuture'>
    # return


async def main():
    start = now()
    url = r"https://www.baidu.com/s?ie=UTF-8&wd=requests%20%E5%BC%82%E6%AD%A5"

    get = fetch(url)
    tasks = [asyncio.ensure_future(get)]
    # # 0 方式 直接获取结果 推荐使用
    for task in asyncio.as_completed(tasks):
        data = await task
        print(type(data))
    # tasks = await asyncio.gather(*tasks)
    # # for v in tasks:
    # #     # data = await task
    # #     print(v, type(v))
    # # abc = asyncio.run(tasks)
    # # print(abc)
    # return await asyncio.gather(*tasks)

    # 老方法
    # loop = asyncio.get_event_loop()
    # tasks = [asyncio.ensure_future(test(1)), asyncio.ensure_future(test(2))]
    # return await asyncio.gather(*tasks)

    # 0 方式 直接获取结果  推荐使用
    # for task in asyncio.as_completed(tasks):
    #     data = await task
    #     print(data)

    # 1 方式  推荐使用
    # data = await asyncio.gather(*tasks)
    # for rev in data:
    #     print(rev)
    # return await asyncio.wait(tasks)#用于返回给外部处理结果

    # 2 方式  返回两个参数  不推荐使用
    # data, _ = await asyncio.wait(tasks)
    # for rev in data:
    #     print(rev.result())
    # return await asyncio.wait(tasks)#用于返回给外部处理结果

    # loop.run_until_complete(asyncio.wait(tasks))
    # tasks = [test(), test()]
    # asyncio.run(tasks)
    # res = loop.run_until_complete(data)

    # print(data, 11111111,  res)

    # loop = asyncio.get_event_loop()
    # task = loop.create_task(fun)  # 创建任务
    # loop.run_until_complete(task)
    # a = await fun

    # 1. 实现方式
    # fun = test()
    # tasks = [test(), test()]
    # asyncio.run(tasks)

    # 2. 实现方式
    # 传统方式 先创建事件循环 再加入要运行的异步函数
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(test())  # 注册到事件循环并运行

    # 3. 实现方式  以任务的方式创建
    # loop = asyncio.get_event_loop()
    # # task = asyncio.ensure_future(fun)  # 创建任务  同下
    # task = loop.create_task(fun)         # 创建任务        同上
    # task.add_done_callback(callback)
    # loop.run_until_complete(task)
    # print(task.result(), 44444)  # result 方法用于获取 return 结果 或者用绑定函数
    print("共花费", now()-start)


# 传统方式 先创建事件循环再执行
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# py3.7 run新方法可代替上面两条代码

url = r"https://www.baidu.com/s?ie=UTF-8&wd=requests%20%E5%BC%82%E6%AD%A5"
get = fetch(url)


abc = asyncio.run(get)

print(abc, 22222, 444444444444)


# asyncio.wait 返回结果有两个 一个是结果一个是运行状态
# results, _ = loop.run_until_complete(main())
# for v in results:
#     print(v.result(), 222, _)
