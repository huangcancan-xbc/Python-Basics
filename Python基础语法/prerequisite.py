flag = True
a = input('随便输入')
if flag:
    flag = False
    print(f'flag 已经修改成 False 了！')
else:
    print('False')

if a:
    print(f'你输入的内容是：{a}')
elif a == 0:
    print('你输入的是 0')


a = 1
b = 2
if a == 1:
    print('a 等于 1')
    if b == 2:
        print('b 等于 2')
        print('a 等于 1，b 等于 2')

a = int(input("请输入一串数字"))
if a % 2 == 0:
    print('你输入的数字是偶数')
else:
    print('你输入的数字是奇数')


shu = int(input('请输入一个数字'))
if shu > 0:
    print("这个数是一个正数")
elif shu == 0:
    print("这个数是一个零")
else:
    print("这个数是一个负数")

nian = int(input('请输入一个年份'))
if (nian % 4 == 0 and nian % 100 !=0) or nian % 400 == 0:
    print('这个年份是一个闰年')
else:
    print("这个年份是一个平年")


if 1 == 1:
    pass    # 空语句，用来占位
else:
    print("不可能")
