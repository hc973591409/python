# 列表
name_list = ["小张","小王","小李"]
# 元素增加
name_list.append('翠花')
# for name in name_list:
#     print(name)
print(name_list)

a = [1,2]
b = [3,4]
c = [5]
a.extend(b)
a.append(c)
# extend 合并列表 ，append会把列表作为一个元素插入
# [1, 2, 3, 4, [5]]
print(a)

a = [0,1,2]
# 指定位置插入元素
a.insert(1,3)
print(a)

# 修改列表数据
name_list[1] = 'xiaohu'
print(name_list)

# 查找元素 in(存在) not in （不存在）
name1 = 'xiaohu'
if name1 in name_list:
    print('find it')
else:
    print("not find")

a = ['a','b','c','a','e','f']
print(a.index('a',1))  # 左闭右开区间 找不到就报错

# 删除元素
del a[-1] # 删除最后一个元素
print(a)
a.pop()  # 删除最后一个元素
print(a)
a.remove('a')  # 多个匹配只删除第一个 
print(a)

a = [1,9,2,6,3,6,4]
a.sort()       # 默认升序
print(a)
a.sort(reverse=True)       # 降序需要指定参数
print(a)
a.reverse()       # 列表反转
print(a)

