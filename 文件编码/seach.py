#3、文件查找
#	Cat a.txt
#	Hello world
#	Hello hello world    统计文件中hello 的个数
import re
b='Cat a.txt Hello world hello Hello world'
with open('a.txt','w+') as find:
    f=find.write(b+'\n')
    find.seek(0)
    f=find.read()
    print(f)
res=re.findall('[hello]{5}.*?',f)
print(res)
for i in range(len(res)):
    i=i+1
print('hello的个数是：',i)
    
