#4、文件内容替换
#把a.txt中hello替换为csvt，并保存结果到文件a2.txt中
import re
with open('a.txt','r+') as f,open('a2.txt','w+') as f1:
    res=f.read()
    print(res)
    h =re.sub('hello','csvt',res)
    #res.flush()
    res=f1.write(h)
    
    #print(res)
