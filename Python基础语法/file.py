f = open('list.py', 'r')
print(f)
print(type(f))
f.close()

# 直接 w 方式打开文件，会清空文件内容
f = open('file.py','w')
f.close()

f = open('file.py','w')
f.write('hello world')
f.close()

f = open('file.py','a')
f.write('\nhello world')
f.close()

f = open('file.py','r',encoding='utf-8')
ret = f.read(1000)
print(ret)
f.close()

f = open('file.py','r',encoding='utf-8')
for line in f:
    print(line,end='')  # 读到文件末尾时，会自动换行，print 打印又会添加一个换行符。给 print 添加 end=''，可以解决这个问题。
f.close()

f = open('file.py','r',encoding='utf-8')
line = f.readline()
print(line)
f.close()

# 上下文管理器
with open('file.py','r',encoding='utf-8') as f:
    line = f.readline()
    print(line)





