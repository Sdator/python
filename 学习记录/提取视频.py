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
import sys
import time
import asyncio
import requests
from functools import partial

# 取当前时间


def now(): return time.time()


async def fetch(url, data, headers):
    # 利用 run_in_executor 把普通函数转为异步函数
    future = asyncio.get_event_loop().run_in_executor(
        None, partial(requests.post, url, data=data, headers=headers))
    return await future


class A:
    time = time.time()

    async def 获取课程(self, 视频列表id=1802061):
        body = '''callCount=1
scriptSessionId=${scriptSessionId}190
httpSessionId=3f847fddcc124945b1a2148bd4839f41
c0-scriptName=PlanNewBean
c0-methodName=getPlanCourseDetail
c0-id=0
c0-param0=string:%s
c0-param1=number:0
c0-param2=null:null
batchId=%s''' % (视频列表id, self.time)
        url = 'https://study.163.com/dwr/call/plaincall/PlanNewBean.getPlanCourseDetail.dwr?%s' % int(
            self.time)
        headers = {
            'Content-Type': 'text/plain',
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
            "providerid": "9660634",
            'cookie': '_ntes_nnid=d9614f93954b2dca52ead1635aa88fa1,1571159295431; _ntes_nuid=d9614f93954b2dca52ead1635aa88fa1; _antanalysis_s_id=1571159295782; mail_psc_fingerprint=cfb29001217d55a4ca46a1f249b6ba53; vjlast=1572890506.1572890506.30; vjuids=d3c75609.16e379474dc.0.37401f27b7da9; usertrack=ezq0J15CLs628FC9Ayy2Ag==; UM_distinctid=170cf4202f0b61-03e8510f2598e3-4313f6a-1fa400-170cf4202f1a95; NTES_SESS=Y1spcm3BNkdu2X7mPYv2k.rZV9WpGlGPkC85EdrnEZ3HdWG74r.5xssvmQ9Ji_fr5ngohZk0592ohii8osnvBN.m7an24sWL8N6nPTgsFbyZa0A30n8yW2jn3CQ2o_3AoZYK6iCUyFhKVuMvoLXvz9r_b2go_F3EVNv4zUzWeAbAttRRKeTMi1CVrYkHrQ4ykuWD9UV4mqjFzOhbtCuPhZ19y; S_INFO=1584898692|0|##|250740270@qq.com; P_INFO=250740270@qq.com|1584898692|1|iplay|00&13|gud&1584898680&iplay#gud&445300#10#0#0|&0|iplay|250740270@qq.com; NTES_CMT_USER_INFO=41940272%7C250740270%40qq.com%7Chttp%3A%2F%2Fcms-bucket.nosdn.127.net%2F2018%2F08%2F13%2F078ea9f65d954410b62a52ac773875a1.jpeg%7Cfalse%7CMjUwNzQwMjcwQHFxLmNvbQ%3D%3D; s_n_f_l_n3=14af3d27ef0995451589120892815; ne_analysis_trace_id=1589489782244; vinfo_n_f_l_n3=14af3d27ef099545.1.22.1575382929761.1589114568524.1589489800444; NTESSTUDYSI=3f847fddcc124945b1a2148bd4839f41; EDUWEBDEVICE=03ae94bcfb534977ba32ef9e3501adcf; eds_utm=eyJjIjoiIiwiY3QiOiIiLCJpIjoiIiwibSI6IiIsInMiOiIiLCJ0IjoiIn0=|aHR0cHM6Ly93d3cuYmFpZHUuY29tL2xpbms/dXJsPWZmZkRwNFRTa2MwMVB5SUpCWFFIbzRFUkZ4Z1NCa3ptVVFxbWR3X1NZSWxoVDloNm1HUkNlUTd4TEFaVjhKTWF3RmN6QjJIUDFMaURSMWNrUm8tTmxfJndkPSZlcWlkPTk2MGM1NWNmMDAwMjFkMjcwMDAwMDAwNjVmMjAzYzdl; hb_MA-BFF5-63705950A31C_source=www.baidu.com; EDU-YKT-MODULE_GLOBAL_PRIVACY_DIALOG=true; STUDY_MIND_TELBIND=1; NETEASE_WDA_UID=1022824062#|#1481636993220; STUDY_PRIVACY_CONFIRMED=1; videoResolutionType=3; _ntes_newsapp_install=false; STUDY_SESS="fUMcLnwwhCkdUHRJO5qEfwML/V1tfsrZA9l638D6p2eeCDpci82A7dmsAL0lxVuG3Na9HONg0aKphweM3XGt822mQjPax+SX3FrXMcyWLd5u+dTqXEM78gZIOTKfkfunHv669nDoEUOM8dYuVaDe/jjyBVBQfRlXjFnrJ/65nMoE5hl6xraugQQKVh+ytkrT+P6MxCmnJEvne6pPMc9TTJJnThNrM7aj0X5LVpSBvjbYOYkpV4njbv/TPu60F2P+LlNXSlyLq8EcnvQsSnzKsi3IfUZjPMF5A7Dh8eHwaGxKlOh/Gwx6G1S/X4FQ7qd/iwuy5z/cc9SHjZR20/lQr2Yhry1X6jTAOqc11qLtuQyTYG7ctes9eQ4RTAPDJMZG"; STUDY_INFO=UID_E2D6111D218EFC805D301515FA4FEFB1|4|1022824062|1596309540074; hasVolume=true; videoRate=1; 1022824062=1022824062; videoVolume=1; STUDY_UUID=24c7b955-e82d-4fe6-8b77-091bf63a12f7; utm=eyJjIjoiIiwiY3QiOiIiLCJpIjoiIiwibSI6IiIsInMiOiIiLCJ0IjoiIn0=|aHR0cHM6Ly9zdHVkeS4xNjMuY29tL2NvdXJzZS9jb3Vyc2VMZWFybi5odG0/Y291cnNlSWQ9MTUxMjAwNw=='
        }
        res = await fetch(url, body, headers=headers)
        return res

    async def 获取视频地址():
        视频ID = 123
        列表ID = 465
        url = "https://study.163.com/dwr/call/plaincall/LessonLearnBean.getVideoLearnInfo.dwr?%s" % int(
            self.time)
        body = '''callCount=1
    scriptSessionId=${scriptSessionId}190
    httpSessionId=3f847fddcc124945b1a2148bd4839f41
    c0-scriptName=LessonLearnBean
    c0-methodName=getVideoLearnInfo
    c0-id=0
    c0-param0=string:%s
    c0-param1=string:%s
    batchId=1596230378140
    ''' % (视频ID, 列表ID)
        head = {
            "providerid": window.ownerId,
            "content-type": "text/plain"
        }


async def main():
    a = A()
    课程 = await a.获取课程()
    print(课程.text)

asyncio.run(main())
