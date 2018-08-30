# 公共方法
# +	[1, 2] + [3, 4]	[1, 2, 3, 4]	合并	字符串、列表、元组
# *	'Hi!' * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	复制	字符串、列表、元组
# in	3 in (1, 2, 3)	True	元素是否存在	字符串、列表、元组、字典
# not in	4 not in (1, 2, 3)	True	元素是否不存在	字符串、列表、元组、字典
print([1,2]+[3,4])
print("hello "+'world')
print('HI '*4)
print(3 in (1,2,3))
print(7 not in (1,2,3))
# in 在字典中只判断key
info = {'name':'班长',
        'id':100,
        'sex':'f',
        'address':"地球亚洲北京"}

# 判断value
print('班长' in info.values() )
# 1	cmp(item1, item2)	比较两个值
# 2	len(item)	计算容器中元素个数
# 3	max(item)	返回容器中元素最大值
# 4	min(item)	返回容器中元素最小值
# 5	del(item)	删除变量

a = [1,2]
b = [3,4]
print(len(a)==len(b))

print(max(a))
print(max(b))
print(min(a))
print(min(b))

# 可变类型，值可以改变：

# 列表 list
# 字典 dict
# 不可变类型，值不可以改变：

# 数值类型 int, long, bool, float
# 字符串 str
# 元组 tuple
