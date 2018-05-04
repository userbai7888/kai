# 文件复制
'''with open('test.txt','r') as read_f,open('test1.txt','w+') as write_f:
    data=read_f.read()
    data=write_f.write(data)'''
# 图片复制
with open('176817195_49.jpg','rb') as img_f,open('123.jpg','wb') as write_img:
    data=img_f.read()
    data=write_img.write(data)
