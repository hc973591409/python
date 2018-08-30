# str遍历
str_1 = '1234abcd'
for ch in str_1:
    print(ch,end=',')

print("")

# 列表遍历
list_1 = [1,2,3,4,5,6,7,8,9]
i = 0
for li in list_1:
    print('%d %d' %(i,li),end=',')
    i += 1
print("")

# 元组遍历
tuple_1 = (9,8,7,6,5,4)
i = 0
for item in tuple_1:
    print("%d %d" %(i,item),end=',')
    i += 1
print("")

# 字典遍历
info = {'name':'班长',
        'id':100,
        'sex':'f',
        'address':"地球亚洲北京"}

for key in info.keys():
    print(key,end=',')
print("")

for value in info.values():
    print(value,end=',')
print("")

for item in info.items():
    print(item, end=',')
print("")