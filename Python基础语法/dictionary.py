a = {}
print(type(a))

a = {
    'name': 'zhangsan',
    'age': 18,
    'sex': 'male',  # 最后一个元素后面的逗号可写可不写
}
print(a)
# in 只是 判断 key 是否存在，和 value 无关
print('name' in a)
print('id' in a)

# not in 用来判断 key 是否不存在
print('name' not in a)
print('id' not in a)

# 使用 [] 来根据key 获取 value
print(a['name'])
print(a['age'])

a['id']=100
print(a)
a['id']=200
print(a)

a.pop('id')
print(a)
a.pop('name')
print(a)

for key in a:
    print(key)
    print(key, a[key])

print(a.keys())
print(a.values())
print(a.items())

for key, value in a.items():
    print(key, value)


print('--------------------------------------------------------')
# hash 函数:不可变的对象，一般是可哈希的；可变的对象，一般不可哈希
print(hash('zhangsan'))
print(hash(3.14))
print(hash(True))
print(hash(()))
# print(hash([1, 2, 3]))