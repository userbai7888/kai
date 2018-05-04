import socket
s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#全循环
while True:
    data=input('白：') 
    #给服务器发送数据和地址，进行数据请求
    s.sendto(data.encode(),('localhost',8080))
    #接受来自服务器端单的数据
    data,addr=s.recvfrom(1024)
    #打印数据，并解码
    print('余：',data.decode())
s.close
