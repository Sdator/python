# -*- coding: utf-8 -*-


# from AirCom import *
'''
from socket import *
from time import ctime

地址 = ''
端口 = 9090
BUFSIZ = 1024
ADDR = (地址, 端口)
# 创建TCP Socket
tcpSerSock = socket(AF_INET, SOCK_STREAM)
# 不过不加这一句的后果就是上面的端口不能再复用
tcpSerSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# 绑定套接字
tcpSerSock.bind(ADDR)
# 监听
tcpSerSock.listen(5)
# 循环获取客户端消息
while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send('get your data:%s\n[%s]' % (data, ctime()))

        tcpCliSock.close

tcpSerSock.close
'''

# 这是一个函数 带两个参数  我们叫这种做形参

# 变量 整形和实数
a = 100
b = 1.222

# 变量 字符串类型
test = "你大爷"
test1 = "你妹子"

# 变量 布尔类型只有真和假 即  true和false
b = a < b


if b:
    # 如果b等于真就
    print(test)
else:
    # 否则就
    print(test1)

