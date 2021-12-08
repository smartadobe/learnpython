import socket

def make_server(ip, port, app): # 代表server
    # 处理套接字通信相关事宜
    sock = socket.socket()
    sock.bind((ip, port))
    sock.listen(5)
    print('Starting development server at http://%s:%s/' %(ip,port))
    while True:
        conn, addr = sock.accept()

        # 1、接收并处理浏览器发来的请求信息
        # 1.1 接收浏览器发来的http协议的消息
        recv_data = conn.recv(1024)

        # 1.2 对http协议的消息加以处理，简单示范如下
        ll=recv_data.decode('utf-8').split('\r\n')
        head_ll=ll[0].split(' ')
        environ={}
        environ['PATH_INFO']=head_ll[1]
        environ['method']=head_ll[0]

        # 2：将请求信息处理后的结果environ交给application，这样application便无需再关注请求信息的处理，可以更加专注于业务逻辑的处理
        res = app(environ)

        # 3：按照http协议向浏览器返回消息
        # 3.1 返回响应首行
        conn.send(b'HTTP/1.1 200 OK\r\n')
        # 3.2 返回响应头（可以省略）
        conn.send(b'Content-Type: text/html\r\n\r\n')
        # 3.3 返回响应体
        conn.send(res)

        conn.close()

def app(environ): # 代表application
    # 处理业务逻辑
    return b'hello world'

if __name__ == '__main__':
    make_server('127.0.0.1', 8008, app)