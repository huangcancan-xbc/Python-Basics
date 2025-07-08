def sum(a,b):
    return a+b

s = sum(1,2)
print(s)

s = sum(46.41324,56.66591)
print(s)

def p():
    print('hello')
    print('hello')
    print('hello')
    print('hello')
p()

def func(a,b,c):
    return c+a+b

print(func("dashdk","dsakh","4566"))
print(func(1,2,3))
print(func(1.454,-54684,33544))

a = 10.5
b = 100
def func(a,b):
    a *= 10
    return a+b, a

def get():
    a = 10
    b = 20
    return a, b
x, y =get()
print(x,y)

_, y = get()
print(y)

def p():
    print(y)

p()


q = 10
def gai():
    global q
    q = 1000

gai()
print(q)


def factor(n):
    if n== 1:
        return 1
    return n * factor(n-1)

print(factor(5))

def temp(a,b):
    print(f'a={a}')
    print(f'b={b}')

temp(20, 10)
temp(b = 10, a= 20)