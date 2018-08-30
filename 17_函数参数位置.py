def f(a,b,c):
    return a+b-c

print(f(1,2,3))
# 指定参数传入
# 要指定就都指定，不能指定一些不指定一些
print(f(c=1, a=2, b=3))

# 利用元组接受多参数，多返回值
def divv(a,b):
    shang = a//b
    yushu = a%b
    return shang, yushu 
# 顺序不能反，只能全部接受，不能用两个接受三个这种做法
shang,yushu = divv(5,2)
print("%d %d" %(shang, yushu))

# 默认参数, 带有默认参数的函数，默认参数必须放在最后
def printf(name, age=18):
    print(name)
    print(age)

printf('Mike')
printf('Json',20)
printf(age=22, name='Coco')

# 递归 求阶乘
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(4))

# 匿名函数，lambda函数
# (lambda x,y:x+y)(1,2)   (lambda x,y:x+y)函数体  x,y:x+y形参以及返回值  (1,2)实参及传递的参数
print((lambda x,y:x+y)(1,2))

# 利用lambda把函数作为参数传递
def calc(a, b, func):
    return func(a,b)
# 用户输入lambda表达式 
print(calc(1, 2, lambda x,y:x+y))
# expression = eval(input('用户输入lambda表达式 如lambda x,y:x+y'))
# print(calc(1, 2, expression))

# 利用lambda实现 列表的其他元素排序
stus = [
    {"name":"zhangsan", "age":18}, 
    {"name":"lisi", "age":19}, 
    {"name":"wangwu", "age":17}
]
stus.sort(key=lambda i:i['age'])   # sort的排序内容关键字key
print(stus)