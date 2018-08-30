# 与电脑玩剪刀石头布
# （1）剪刀 （2）石头 3（布）
import random
# 导入随机数模块
def main():
    player = int(input("请输入（1）剪刀 （2）石头 3（布）："))
    rand_list = [1,2,3]
    compter = random.choice(rand_list)
    print('compter = %d  player = %d' %(compter, player))
    if ((player == 1 and compter == 3) or (player == 2 and compter == 1) or (player == 3 and compter == 2)):
        print('U WIN')
    elif player == compter:
        print("再来一局")
    else:
        print('U LOSE')

if __name__ == '__main__':
    main()