a = []
print(type(a))

b = list()
print(type(b))

# 下标访问
c = [1,2,3,4,5]
print(c[0])
print(c[len(c) - 1])
print(c[-1])
print(c[1:3]) # 切片：从下标1开始，到下标3结束，不包含下标3（左闭右开）
print(c[1:])
print(c[:3])
print(c[:])

c[3] = 10
print(c,len(c))

b = [1,2,3,4,5,6,7,8,9,10]
print(b[::2])# 第三个参数表示步长，表示每隔2个取一个
print(b[::-1])
print(b[:20])

for x in b:
    print(x)

for i in range(0,len(b)):
    print(b[i])
    b[i] = b[i] * 2
    print(b[i])

i = 0
while i < len(b):
    print(b[i])
    i = i + 1

b.append("dashkjhdkashdkj")
b.insert(2,"fsdkhfjku")
b.insert(100,'dfhus')
print(b)

# in 用于判断某个元素是否在列表中
print('dskhja' in b)
print('dfhus' in b)

# index 用于获取某个元素的下标
print(b.index(4))

b.pop()
b.pop()
b.pop()
print(b)
b.pop(2)    # 删除下标为2的元素
print(b)

# remove 用于删除某个元素
b.remove(4) # 删除值为4的元素
print(b)

# 使用 + 运算符连接两个列表，注意：连接后的列表是两个列表的副本，而不是两个列表的引用
a.append('4654646')
c = a + b
print(c)

# extend 用于连接两个列表，相比 += ，extend 更快，所以 使用 extend 更好
b.extend(a)
print(b)
print(a)
c=b.extend(a)
print(c)

b+=a+b+b
print(b)
