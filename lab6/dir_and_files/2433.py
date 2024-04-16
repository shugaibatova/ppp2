import re
a=open(r"dir_and_files\1332.txt",'r',encoding='UTF-8')
s=a.read()
def squares(text):
    for i in range(1,text+1):
        yield i**2
list=int
for a in squares(s):
    list=a
with open("12.txt",'w') as file:
    file.write(list)


