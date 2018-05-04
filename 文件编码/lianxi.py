#5.练习将列表、元组和字典保存到文件中，并且进行读取，输出每一个元素
import json
mylist=[1,3,4,4,3,6,2,78,63,42,5,52,332,5]
mytupl=(35,62,62,57,72,6,26,26,23,52,5,25,)
mydict={'name':'白凯强','age':26,'爱好':'网球'}
with open('练习.txt','w+') as f:
    cotent=json.dumps(mylist)
    cotent1=json.dumps(mytupl)
    cotent2=json.dumps(mydict)
    f.write(cotent2+'\n')
   # f.write(cotent1+'\n')
    #f.write(cotent2)
    f.flush()
    f.seek(0)
    res=json.loads(f.read())
    #res1=json.loads(f.read())
    #res2=json.loads(f.read())
    print(res)
