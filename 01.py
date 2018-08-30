import keyword


print(keyword.kwlist)
# 格式化输出
# %c	字符
str1 = 'A'
print('%c' %str1)
# %s	通过str() 字符串转换来格式化
num = 100
print('%d' %num)
# %i	有符号十进制整数
num = -1
print('num = %u' %num)
# %d	有符号十进制整数
# %u	无符号十进制整数
# %o	八进制整数
num = 100
print('%o' %num)
# %x	十六进制整数（小写字母）
num = 100
print('%x' %num)
# %X	十六进制整数（大写字母）
num = 100
print('%X' %num)
num = 100
print('%e' %num)
# %e	索引符号（小写'e'）
num = 100
print('%E' %num)
# %E	索引符号（大写“E”）
# %f	浮点实数
# %g	％f和％e 的简写
# %G	％f和％E的简写

# 打印一个小名片
print("*"*50)
print("姓名：胡超")
print("邮箱：973591409@qq.com")
print("电话：188168909889")
print("*"*50)

# 在python2种，要获得原始字符串，应该用raw_input
# 在python3中，input获取的，都是字符串，获得表达式用eval
exssion = eval(input("输入表达式"))
print(exssion)
# 输入表达式1+9
# 10

# 运算符
print(9.0//2.0)
# //	取整除	返回商的整数部分 9//2 输出结果 4 , 9.0//2.0 输出结果 4.0
print(9.0%2.0)
# %	取余	返回除法的余数 b % a 输出结果 0
print(9.0**2.0)
# **	幂	返回x的y次幂 a**b 为10的20次方， 输出结果 100000000000000000000

# +=	加法赋值运算符	c += a 等效于 c = c + a
# -=	减法赋值运算符	c -= a 等效于 c = c - a
# *=	乘法赋值运算符	c *= a 等效于 c = c * a
# /=	除法赋值运算符	c /= a 等效于 c = c / a
# %=	取模赋值运算符	c %= a 等效于 c = c % a
# **=	幂赋值运算符	c **= a 等效于 c = c ** a
# //=	取整除赋值运算符	c //= a 等效于 c = c // a