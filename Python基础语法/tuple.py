a = ()
print(type(a))

a = (10,10,20,20,30,30,100,100)
print(a[5])
print(a[1:5])
print(a[1::2])

for x in a:
    print(x)

print(50 in a)
print(50 not in a)# not in表示不在

# 元组不支持修改
# a [2]=100
# print(a)
# a.append(100)
# a.extend([100,200])
# a.pop()
# print(a)
