# 元组类型，是不可变类型，不可以增删
# 定义元组
a = (1,2,2,4,5,2,8)
print(a[2])
# 求元素个数，和str用法一样
print(a.count(2))
# 和和str用法一样，都是左闭合，右开区间
print(a.index(2,2,5))
for i in a:
    print(i,end=",")

# 定义空元组
b = ()
print(type(b))
print(b)

# 只有一个元素的元组
b = (1, )           # 只有一个元素必须加上，否则会解析为基本数据类型
print(type(b))
print(b)