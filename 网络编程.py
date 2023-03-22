#_*_coding:utf-8_*_
__author__ = 'Linhaifeng'
import socket
ip_port=('127.0.0.1',9011)  #电话卡
BUFSIZE=1024                #收发消息的尺寸
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #买手机
# s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(ip_port) #手机插卡
s.listen(3)     #手机待机

while True:
    conn,addr=s.accept()            #手机接电话
    print(conn)
    print(addr)
    print('接到来自%s的电话' %addr[0])
    while True:
        msg=conn.recv(BUFSIZE)             #听消息,听话
        if len(msg)==0: break
        print(msg,type(msg))

        conn.send(msg.upper())          #发消息,说话

    conn.close()                    #挂电话

s.close()                       #手机关机