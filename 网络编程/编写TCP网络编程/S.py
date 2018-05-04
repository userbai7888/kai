#引入一个socket
import socket
from threading import Thread
#创建套接字
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定地址
s.bind(('localhost',8080))
#开始监听
s.listen()
#接受请求链接
print('数据传输中......')
conn,addres=s.accept()
#创建一个接受的函数
def my_recv(data):
    while True:
        res=conn.recv(1024).decode()  #接受请求数据
        if res=='exit':  #接受客户端传来的请求，然后解码，进行判断
            break
        print(res)
if __name__=='__main__':
    t=Thread(target=my_recv,args=(conn,))
    t.start()
    while True:
        try:
            data='服务器：'+input('')
            if data=='exit':
                break 
            else:
                conn.send(data.encode())
        except Exception as e:
            print('错了')
            break
    s.close()

