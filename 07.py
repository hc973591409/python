# 字符串常见操作
# 1.find
my_str = 'hello world hello C hell CPP hello Python'
print(my_str.find("worxd"))    # 返回匹配的第一个值索引 找不到返回-1
print(my_str.index("world"))   # 返回匹配的第一个值索引 找不到会报异常
print(my_str.count("hello", 0, len(my_str))) # 返回两个参数可以不用指定，返回出现个数
# 可以连续替换，返回一个新的字符串
print(my_str.replace("hello", "hi",my_str.count("hello")))  #hi world hi C hell CPP hi Python

str1 = "123#fadsf#fdsff@qq.com"
str_list = str1.split('#')
print(str_list)
# 字符串切割函数只能指定一个分隔符，要指定多个分隔符等用到正则
# ===============================================================
import re
str2 = "123#fadsf fdsff@qq,com"
pattern = re.compile(r'#| |,')
str2_list = re.split(pattern,str2)
print(str2_list)

str3 = 'hello world'
# 第一个字母大写
print(str3.capitalize())
# 开头的每个字母都大写
print(str3.title())
# 判断是不是以指定的字符串开头
print(str3.startswith('hello'))
print(str3.startswith('Hello'))
# 判断是不是以指定的字符串结束
print(str3.endswith('world'))
print(str3.endswith('World'))
str3 = 'HELLO world'
# 字符串转为小写
print(str3.lower())
print(str3.upper())
# 左对齐打印，按20个字符对齐
print(str3.ljust(20))
print(str3.rjust(20))
print(str3.center(20))

# 删除空白符，包括 \r\n\t
str3 = '  \r\n\t  HELLO world    \r\n\t  '
print(str3.strip())

str4 = "hello world hell c hello cpp"
print(str4.partition('c'))
str4 = "hello world hell c hello cpp"
print(str4.rpartition('c'))
str5 = 'hello world\nhello c\nhellocpp'
# 按行分割，存成一个字符串列表
print(str5.splitlines())
print('*'*50)
str6 = 'huchao'
# 判断字符串是不是都是字母
print(str6.isalpha())
str6 = '12345'
# 判断字符串是不是都是字母
print(str6.isdigit())

str6 = '12345abcd'
# 判断字符串是不是都是字母或者数字
print(str6.isalnum())

# 判断是否只是包含空格
str7 = ' '
print(str7.isspace())

li = ['my','name','is','huchao']
str8 = ' '
# 用str作为分隔符，连接列表里面的字符串
print(str8.join(li))
