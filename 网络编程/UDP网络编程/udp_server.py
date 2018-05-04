import socket
#创建socket套接字
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定地址和端口
s.bind(('localhost',8080))
print('信息传输中......')
#全循环
while True:
    #接受客户端发来的请求，发一个数据和地址
    data,addr=s.recvfrom(1024)
    #打印请求的数据并把它解码出来
    print('白：',data.decode())
    data=input('余：')
    #发送给客户端的数据，并且编码
    s.sendto(data.encode(),addr)
s.close
