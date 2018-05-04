with open(r'test.txt','a+') as f:
    res=f.read()#读取文件内容
    print(res)
    res=f.write('见到你，心就澎湃。')#给文件写东西
    f.seek(0)#指针指向第一个字符
    res=f.read()#读取写入文件的内容
    print(res)

