
# -*- coding: utf-8 -*-
'''
依赖包
    Six
    transmissionrpc
安装依赖包
    pip3 install transmissionrpc Six -i https://pypi.tuna.tsinghua.edu.cn/simple
    python3 -m pip install transmissionrpc Six -i https://pypi.tuna.tsinghua.edu.cn/simple

'''


# print(dir(transmissionrpc))

# tc = client.Client(address='127.0.0.1', port=9091)


import transmissionrpc

# info = {"address": "hxun.xyz:20001", "port": 9091,
#         "user": "liusikair", "password": "19920818ol"}

# 登录客户端获取句柄
# tc = transmissionrpc.Client(）
tc = transmissionrpc.Client(
    address='127.0.0.1', port=9091, user="liusikair", password="19920818ol",)

# Trackers
# ListCollection

# tc.change_torrent()


def 下载(url):
    '''
    参数1 地址
    '''
    tc.add_uri(url)
    tc.add_torrent()


if __name__ == "__main__":
    # 下载(r"magnet:?xt=urn:btih:DTM4A6RF2JYQUOSENUHMDUXI4WQ3SFCQ&dn=&tr=http%3A%2F%2F104.238.198.186%3A8000%2Fannounce&tr=udp%3A%2F%2F104.238.198.186%3A8000%2Fannounce&tr=http%3A%2F%2Ftracker.openbittorrent.com%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker3.itzmx.com%3A6961%2Fannounce&tr=http%3A%2F%2Ftracker4.itzmx.com%3A2710%2Fannounce&tr=http%3A%2F%2Ftracker.publicbt.com%3A80%2Fannounce&tr=http%3A%2F%2Ftracker.prq.to%2Fannounce&tr=http%3A%2F%2Fopen.acgtracker.com%3A1096%2Fannounce&tr=https%3A%2F%2Ft-115.rhcloud.com%2Fonly_for_ylbud&tr=http%3A%2F%2Ftracker1.itzmx.com%3A8080%2Fannounce&tr=http%3A%2F%2Ftracker2.itzmx.com%3A6961%2Fannounce&tr=udp%3A%2F%2Ftracker1.itzmx.com%3A8080%2Fannounce&tr=udp%3A%2F%2Ftracker2.itzmx.com%3A6961%2Fannounce&tr=udp%3A%2F%2Ftracker3.itzmx.com%3A6961%2Fannounce&tr=udp%3A%2F%2Ftracker4.itzmx.com%3A2710%2Fannounce&tr=http%3A%2F%2Ftr.bangumi.moe%3A6969%2Fannounce&tr=http%3A%2F%2Ft.nyaatracker.com%2Fannounce&tr=http%3A%2F%2Fopen.nyaatorrents.info%3A6544%2Fannounce&tr=http%3A%2F%2Ft2.popgo.org%3A7456%2Fannonce&tr=http%3A%2F%2Fshare.camoe.cn%3A8080%2Fannounce&tr=http%3A%2F%2Fopentracker.acgnx.se%2Fannounce&tr=http%3A%2F%2Ftracker.acgnx.se%2Fannounce&tr=http%3A%2F%2Fnyaa.tracker.wf%3A7777%2Fannounce&tr=http%3A%2F%2Ft.nyaatracker.com%3A80%2Fannounce&tr=https%3A%2F%2Ftr.bangumi.moe%3A9696%2Fannounce&tr=http%3A%2F%2Ft.acg.rip%3A6699%2Fannounce&tr=http%3A%2F%2Ftracker3.itzmx.com%3A6961%2Fannounce&tr=http%3A%2F%2Fopen.acgnxtracker.com%2Fannounce&tr=http%3A%2F%2Fsukebei.tracker.wf%3A8888%2Fannounce&tr=http%3A%2F%2Ftracker.kamigami.org%3A2710%2Fannounce&tr=https%3A%2F%2Ftracker.nanoha.org%2Fannounce")
