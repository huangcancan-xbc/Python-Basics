n = 10
while n:
    print(n)
    n -= 1

num = 1
sum = 0
while num <= 100:
    sum += num
    num += 1

print(sum)


# 计算1到5每个数的阶乘
arr = 1
ret = 0
while arr <= 5:
    temp = 1
    i = 1
    while i <= arr:
        temp *= i
        i += 1
    arr += 1
    ret += temp

print(ret)


# for循环，range:左闭右开区间，第三个参数表示步长
for i in range(1,11):
    print(i)

for i in range(1, 11, 3):
    print(i)

for i in range(50, 0, -10):
    print(i)


for i in range(0,20):
    if i == 10:
        continue
    if i == 15:
        break
    if i % 2 ==0:
        print(f'这是第{i}个数，并且是偶数')
    else:
        print(f'这是第{i}个数，并且是奇数')




total_sum = 0  # 总和
count = 0  # 输入的数字个数

while True:
    user_input = input('请输入一个数字（输入";"表示结束）：')

    # 检查是否输入了分号
    if user_input == ';':
        break

    try:
        # 尝试将输入转换为浮点数
        num = float(user_input)
    except ValueError:
        print("输入无效，请输入一个数字或分号';'")
        continue

    # 更新总和和计数
    total_sum += num
    count += 1

# 计算平均数
if count > 0:  # 确保至少输入了一个数字
    average = total_sum / count
    print(f'平均数为：{average}')
else:
    print('没有输入任何数字，无法计算平均数。')


