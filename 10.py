# 有8位老师，随机分到3个办公室

import random
offices = [[],[],[]]

names = ['A','B','C','D', 'E','F','G','H']

for name in names:
    index = random.randint(0,2)
    offices[index].append(name)
    
i = 1
for office in offices:
    print('办公室：%d,人数为：%d' %(i,len(office)))
    i += 1