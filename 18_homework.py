# 1. 编程实现 9*9乘法表
def nine_nine():
    for i in range(1,10):
        for j in range(1,i+1):
            print("%d*%d=%d" %(j,i,i*j),end='\t')

        print('')


# 2.用函数实现求100-200里面所有的素数  提示：素数的特征是除了1和其本身能被整除，其它数都不能被整除的数
def sushu():
    for i in range(100,201):
        tmp = i//2
        flag = True
        for j in range(2, tmp+1):
            if i%j == 0:
                flag = False
                break
        if flag:
            print('素数 %d' %i)
            

# 3.请用函数实现一个判断用户输入的年份是否是闰年的程序

# 提示：
# 1.能被400整除的年份 
# 2.能被4整除，但是不能被100整除的年份
# 以上2种方法满足一种即为闰年
def leaf(year):
    # year = int(input("请输入年"))
    if (year%400 == 0 ) or ((year%4 == 0) and (year%100 != 0)):
        print("是闰年")
        return True
    else:
        print("不是闰年")
        return False

# 1.用函数实现输入某年某月某日，判断这一天是这一年的第几天？闰年情况也考虑进去
# 20160818
# 是今年第x天
def calc_day():
    date = input("请输入年")
    rui = [31,29,31,30,31,30,31,31,30,31,30,31]
    rui_f = [31,28,31,30,31,30,31,31,30,31,30,31]
    year = int(date[:4])
    month = int(date[4:6])
    day = int(date[6:])
    # 闰年
    time_day = 0
    if leaf(year):
        if month == 1:
            time_day = day
        else:
            for i in range(1, month):
                time_day += rui[i-1]
            time_day += day
    # 不是闰年
    else:
        if month == 1:
            time_day = day
        else:
            for i in range(1, month):
                time_day += rui_f[i-1]
            time_day += day
    return time_day

    
def main():
    # nine_nine()
    # sushu()
    print(calc_day())

if __name__ == '__main__':
    main()