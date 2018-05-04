#引入一个socket，和Thread的类
import socket
from threading import Thread
#创建套接字
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#链接地址
s.connect(('localhost',8080))
#创建一个接受数据的函数
def my_recv(data):
    while True:
        res=s.recv(1024).decode() #接受请求数据
        if res=='exit':            
            break
        print(res)
if __name__=='__main__':  
    #创建一个线程
    t=Thread(target=my_recv,args=(s,))
    #开始线程
    t.start()
    while True:
        try:
            data='客户端：'+input('') 
            if data=='exit':         #给服务器发送退出的请求，
                break
            else:
                s.send(data.encode()) #发送数据给服务器
        except Exception as e:
            print('错了')
            break
    s.close()