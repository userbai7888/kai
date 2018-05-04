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
res=conn.recv(1024)  #接受请求数据
print('请求是：',res.decode())
conn.send(b'HTTP/1.1 200 OK\r\n\r\n')
#打开网页页面在发送网页信息
with open(r'1111.html','r',encoding='utf-8') as f:
    res=f.read()
conn.send(res.encode())
s.close()

