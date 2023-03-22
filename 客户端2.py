import socket
ip_port=('127.0.0.1',9010)  #电话卡
BUFSIZE=1024                #收发消息的尺寸
c=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #买手机
c.connect(ip_port) #手机插卡

while True:
    msg = input('请输入汉字：').strip()
    if len(msg)==0: continue
    c.send(msg.encode('utf-8'))
    data = c.recv(BUFSIZE)
    print(data)
    print(data.decode('utf-8'))
c.close()                       #手机关机