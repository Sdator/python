import asyncio
import time


def now():
    return time.time()


async def main():
    print(1)
    # 模拟 IO 操作 等待2秒
    await asyncio.sleep(2)
    print(2)


def 旧的写法():
    # 异步函数本身不执行 而是返回一个异步对象 类似js的promise对象
    fun = main()

    # 异步初始化 获取事件循环
    loop = asyncio.get_event_loop()
    # 类似 js 的 Promise.all
    loop.run_until_complete(fun)

#


def 新的写法():
    # 异步函数本身不执行 而是返回一个异步对象 类似js的promise对象
    fun = main()
    # py3.7 的新写法
    asyncio.run(fun)


if __name__ == '__main__':
    old = now()

    新的写法()
    旧的写法()

    print("耗时：{:.2f}秒".format(now() - old))
