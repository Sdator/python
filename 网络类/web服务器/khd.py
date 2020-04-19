from socket import *
 
HOST = 'input your host ip'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)
 
tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)
 
while True:
    data = raw_input('> ')
    if not data:
        break
    tcpCliSock.send(data)
    
    recv_data = tcpCliSock.recv(BUFSIZ)
    if not recv_data:
        break
    print (recv_data)
 
tcpCliSock.close()
