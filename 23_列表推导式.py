# 所谓的列表推导式，就是指的轻量级循环创建列表
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def basic():
    a = [i for i in range(1,11)]
    print(a)
    # 列表推导式嵌套if
    b = [i for i in range(1,11) if i%2==0]
    print(b)
    # 列表推导式与2重循环
    c = [(x,y) for x in range(1,4) for y in range(3,6)]
    print(c)

    # 列表推导式与3重循环
    d = [(x,y,z) for x in range(1,4) for y in range(3,6) for z in range(4,10) if z%2==0]
    print(d)

def f1():
    # 生成一个[[1,2,3],[4,5,6]....]的列表最大值在100以内
    e = [[x,y,z] for x in range(1,99,3) for y in range(2,100,3) for z in range(3,101,3) if (y==x+1) and (z == x+2)]
    print(e)
# 请写出一段 Python 代码实现分组一个 list 里面的元素,比如 [1,2,3,...100]变成 [[1,2,3],[4,5,6]....]
mylist =[i for i in range(1,101)]
# print(mylist)
index = 0
new_list = []
while index <= 100:
    new_list.append(mylist[index:index+3])
    index += 3

print(new_list)