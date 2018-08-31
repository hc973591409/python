x =y=z=1
z = 1
# x = (y = z + 1) 是错误的  我也不知道为啥
print(x)

# 自己实现字符串替换函数
string = "hello world cpp"
def myreplace(string, oldstr, newstr):
    index = string.find(oldstr)
    if index != -1:
        tmpstr = string[:index]
        tmpstr += newstr
        tmpstr += string[index+len(oldstr):]
        return tmpstr

    else:
        return None

print(myreplace(string, 'hello', 'Tom'))

# 在 Python 中,类和对象有什么区别?对象如何访问类的方法? 创建一个对象时做了什么?
# 对象是对类的实例化，相当于车与我们家车的区别     创建一个对象先调用类的new方法分配空间，再调用init函数初始化对象属性等
# 请写出一段 Python 代码实现分组一个 list 里面的元素,比如 [1,2,3,...100]变成 [[1,2,3],[4,5,6]....]
def group():
    mylist =[i for i in range(1,101)]
    index = 0
    new_list = []
    while index <= 100:
        new_list.append(mylist[index:index+3])
        index += 3
    print(new_list)
# 请写出一段 Python 代码实现删除一个 list 里面的重复元素
# 利用set的不重复特性
list_a = [11,22,33,11,22,33]
set_a = set(list_a)
list_a = list(set_a)
print(list_a)
# 设计实现遍历目录与子目录,抓取.pyc 文件
#设计实现遍历目录与子目录,抓取.pyc 文件
import os

def getFiles(dir, suffix):
    # 定义一个列表，用于存放文件路径
    res = []
    # 遍历dir，返回一个三元数组，第一个就是根目录，第二个是目录列表，第三个是文件名
    for root,dirs,filenames in os.walk(dir):
        for x in filenames:   # 遍历所有的文件
            # os.path.splitext(x)拆分文件和扩展名
            i,j = os.path.splitext(x)
            if j == suffix:
                print(os.path.join(root,x))
getFiles("./", '.pyc')


# 写出一个函数,给定参数 n,生成含有 n 个元素值为 1~n 的数 组,元素顺序随机,但值不重复
import random
a = set()
# (1,10)
while len(a) < 10:
    a.add(random.randint(1,11))
b = list(a)
print(b)

# 在不用其他变量的情况下，交换a、b变量的值
a = 10
b = 20
a,b = b,a
print(a)
print(b)
# 如何在一个 function 里设置一个全局变量
# g_num = 100
def func():
    global g_num
    g_num += 10
func()
print(g_num)