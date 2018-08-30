# 1. 编程实现对一个元素全为数字的列表，求最大值、最小值
# 第一种，自定义函数
import random
my_list = []
for i in range(1,11):
    num = random.randint(1,100)
    my_list.append(num)

num_max = my_list[0]

for i in my_list:
    if num_max < i:
        num_max = i

print(my_list)
print(num_max)
# 用方法
print(max(my_list))

# 2. 编写程序，完成以下要求：
# 统计字符串中，各个字符的个数
# 比如："hello world" 字符串统计的结果为： h:1 e:1 l:3 o:2 d:1 r:1 w:1
string = "hello world"
# 利用字典的键值对是不重复的特性
str_dict = {}
for ch in string:
    # 如果字典对应的key有值就累加，没有就新建
    if str_dict.get(ch):
        str_dict[ch] += 1
    else:
        str_dict[ch] = 1

print(str_dict)


# 3. 编写程序，完成以下要求：
# 完成一个路径的组装
# 先提示用户多次输入路径，最后显示一个完成的路径，比如/home/python/ftp/share
path = ''
while True:
    string1 = input("请输入路径，回车继续输入，exit退出")
    if string1 == 'exit':
        break
    else:
        path += '/'+string1

print(path)
    