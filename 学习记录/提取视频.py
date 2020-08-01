import sys
import time
import asyncio
import requests
import functools
'''

# 执行创建异步的两种方法
    # 1 事件循环+执行
    asyncio.get_event_loop
    asyncio.run_until_complete
    # 2 直接创建并运行
    asyncio.run

# 加入任务 tasks
asyncio.create_task
loop.create_task
asyncio.ensure_future

# 三种获取异步结果的方式
asyncio.as_completed
asyncio.wait
asyncio.gather

# 把普通函数转为异步函数 *
asyncio.run_in_executor

# 获取当前 事件循环 句柄
asyncio.get_running_loop

# future 和 线程 可以作为理解异步的扩展知识
    # 携程 future 对象
        asyncio.future
        asyncio.get_running_loop().create_future    #创建 future
        fut.set_result  # future对象 返回异步结果

    # 线程、进程 futures 对象
        concurrent.futures.Future  # Future 对象
        concurrent.futures.thread  # 线程池
        concurrent.futures.process # 进程池
        ThreadPoolExecutor(max_workers=5)  # 创建线程池 最大数量5
        ProcessPoolExecutor(max_workers=5) # 创建进程池 最大数量5

        pool.submit(fun,args)  # 执行线程
'''


# 取当前时间
def now(): return time.time()

# 测试


async def fetch(url):
    # 利用 run_in_executor 把普通函数转为异步函数
    future = asyncio.get_running_loop().run_in_executor(
        None, requests.get, url)
    return await future


async def main():
    start = now()
    url = r"https://www.baidu.com/s?ie=UTF-8&wd=requests%20%E5%BC%82%E6%AD%A5"

    get = fetch(url)
    tasks = [asyncio.ensure_future(get)]
    tasks = await asyncio.gather(*tasks)
    for v in tasks:
        # data = await task
        print(v, type(v))
