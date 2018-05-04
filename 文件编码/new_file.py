#、提示用户输入要新建的文件，打开文件，
#让用户输入要录入的内容，将内容录入到文件中。





a='txt'
n=input('名称：')
c=[n,a]
n='.'.join(c)
with open(n,'w+')as n_file:
    n_file=n_file.write(input('内容：'))
