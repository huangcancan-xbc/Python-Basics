# 比较运算------------------------------------------------------------
s = 'hello'
ss = 'dosage'
print(s == ss)
print(s != ss)
print(s > ss)
print(s < ss)

# 且或运算------------------------------------------------------""
a:int = 46
b = 485;
print(a > 10 and b > 100)
print(a > 10 or b > 100)
print(a !=b and s == ss)

# not表示逻辑取反
print(not a > 10)       # 相当于C++ !a > 10
print(not not a)

# 赋值操作--------------------------------------------
left = right = 100
print(left, right)
left, right = 50, 200
print(left, right)
ll = left = right = rr = 1000
print(ll, left, right, rr)

ll = + 1000; rr += 1000
print(ll, rr)

++ll
print(ll)