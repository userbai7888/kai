#
import socket
#创建套接字
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#创建连接
s.connect(('localhost',8080))
while True:   
    data =input('我：')#输入请求内容
    s.send(data.encode())#发送请求信息
    #接收响应
    res=s.recv(1024)#得到响应结果
    print('--他：',res.decode())#打印出结果
s.close()
