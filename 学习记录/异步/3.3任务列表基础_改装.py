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


old = now()

# 任务列表先于事件循环创建
# 由于事件循环还没创建 所以无法立即使用 create_task 把函数添加到事件循环中
tasks = [
    demo(),
    demo2()
]

# 内部会自动读取列表并添加到任务列表中
done, pending = asyncio.run(asyncio.wait(tasks))

print(done, pending)


print("耗时：{:.2f}秒".format(now() - old))
