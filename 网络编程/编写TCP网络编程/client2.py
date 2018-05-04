#引入一个socket
import socket
#创建套接字
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#链接地址
s.connect(('localhost',8080))
while True:
    data=input('客户端:--->')
    if data=='exit':            #给服务器发送退出的请求，
        s.send(data.encode())   #给发送请求进行编码
        break
        s.close()
    else:
        s.send(data.encode())   #发送请求
        res=s.recv(1024) #接受请求数据
        print('服务器：',res.decode())
s.close()
