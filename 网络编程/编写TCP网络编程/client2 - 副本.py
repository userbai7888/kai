#引入一个socket
import socket
from threading import Thread
#创建套接字
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#链接地址
s.connect(('localhost',8080))


def my_recv(s):
    while True:
        res=s.recv(1024).decode() #接受请求数据
        if res=='exit':            
            break
        print(res)
         
t=Thread(target=my_recv,args=(s,))
t.start()


while True:
    data=input('')
    s.send(data.encode())  
    if data=='exit':            #给服务器发送退出的请求，
        break
s.close()

