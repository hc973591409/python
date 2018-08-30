# 计算1-100的和
def sum_1_100():
    i = 0
    res = 0
    while i <= 100:
        res += i
        i += 1
    return res

# 计算1-100偶数的和
def sum_2_100():
    i = 0
    res = 0
    while i <= 100:
        if i%2 == 0:
            res += i
            print(i)
        i += 1
    return res

# 打印九九乘法表
# i(1-9)*j(1-9) = x
def nine_nine():
    for i in range(1,10):
        for j in range(1,i+1):
            print("%d*%d=%d" %(i,j,i*j),end='\t')
        print("")

# 除了3和3的倍数都打印
def print_3():
    for i in range(1,101):
        if i%3 == 0:
            continue
        print(i)


def main():
    # print(sum_1_100())
    # print(sum_2_100())
    # nine_nine()
    print_3()

if __name__ == '__main__':
    main()