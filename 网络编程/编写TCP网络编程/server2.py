#引入一个socket
import socket
#创建套接字
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定地址
s.bind(('localhost',8080))
#开始监听
s.listen()
#接受请求链接
print('数据传输中......')
conn,addres=s.accept()
while True:
    res=conn.recv(1024)  #接受请求数据
    if res.decode()=='exit':  #接受客户端传来的请求，然后解码，进行判断
        break
        s.close()
    else:
        print('客户端：',res.decode())   #打印客户端输出的数据
        data=input('服务器--->:')        #输入服务器的数据
        conn.send(data.encode())         #给客户端发送编码的数据
s.close()

