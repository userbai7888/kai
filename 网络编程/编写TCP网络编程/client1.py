#引入一个socket
import socket
#创建套接字
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#链接地址
s.connect(('localhost',8080))
#发送请求
s.send('你好'.encode())
#接受请求数据
res=s.recv(1024)
print(res.decode())
s.close()
