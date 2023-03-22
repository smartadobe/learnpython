#_*_coding:utf-8_*_
__author__ = 'Linhaifeng'
from socket import *
ip_port=('127.0.0.1',8083)

tcp_socket_server=socket(AF_INET,SOCK_STREAM)
tcp_socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcp_socket_server.bind(ip_port)
a = tcp_socket_server.getsockname()
print('本地IP和端口%s，%s'%a)

tcp_socket_server.listen(5)


conn,addr=tcp_socket_server.accept()
print('服务端地址和端口是',conn.getsockname())
print(conn.getsockopt())
print(conn.gettimeout())
print('客户端地址和端口是',conn.getpeername())
# print('客户端地址和端口是',tcp_socket_server.getpeername())
print(addr)

data1=conn.recv(30)
data2=conn.recv(10)

print('----->',data1.decode('utf-8'))
print('----->',data2.decode('utf-8'))

conn.close()