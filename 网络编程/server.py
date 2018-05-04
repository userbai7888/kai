#引入socket#数据的传输，数据为bytes类型
import socket
#创建套接字
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#给套接字绑定地址和端口
s.bind(('localhost',8080))
#监听
s.listen(5)
print('我正在等待数据')
#接收链接
conn,address=s.accept()
#接收请求信息
while True:
    res=conn.recv(1024)#recv堵塞
    print('--他：',res.decode())#输出请求信息
    data =input('我：')#输入响应
    conn.send(data.encode())#将响应返回
s.close()

