#引入一个socket
import socket
#创建套接字
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定地址
s.bind(('localhost',8080))
#开始监听
s.listen()
#接受请求链接
conn,addres=s.accept()
#接受请求数据
res=conn.recv(1024)
print(res.decode())
conn.send('你也好'.encode())
s.close()


