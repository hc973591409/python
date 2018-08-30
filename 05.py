# 打印图形
def main():
    i = 1
    flag = False
    while i<= 9:
        if i > 5:
            flag = True
        if not flag:
            print("*"*i)
        else:
            print("*"*(10-i))
        i += 1


if __name__ == '__main__':
    main()