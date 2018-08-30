# 字典，大括号初始化，按键值对存储
# key：value key只能是不可变类型
info = {'name':'班长',
        'id':100,
        'sex':'f',
        'address':"地球亚洲北京"}
# 按照 tuple[key] 访问
print(info['name'])
print(info['id'])
print(info['sex'])
# 当我们不确定是否有某个key的时候
age = info.get('age')    # 获取不到返回none

# info[key] key存在就修改并覆盖，不存在就新建
if not age:
    info['age'] = 19

print(info.get('age'))

# 删除一个元素
del info['id']
print(info.get('id'))
# 清空字典
print('*'*50)

# 求字典长度，同时可以用于字符串，列表，集合，是一个公共方法
print(len(info))
print(info.keys())
# dict_keys(['name', 'sex', 'address', 'age'])
print(info.values())
# dict_values(['班长', 'f', '地球亚洲北京', 19])
print(info.items())
# dict_items([('name', '班长'), ('sex', 'f'), ('address', '地球亚洲北京'), ('age', 19)])

info.clear()

