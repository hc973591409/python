# 自定义一个异常类，判断用户输入密码
class NotNormal(Exception):
    def __init__(self, lenth, atleast):
        self.lenth = lenth
        self.atleast = atleast


def main():
    try:
        s = input('请输入 --> ')
        if len(s) < 3:
            # raise引发一个你定义的异常
            raise NotNormal(len(s), 3)     
    except NotNormal as result:#x这个变量被绑定到了错误的实例
        print('NotNormal: 输入的长度是 %d,长度至少应是 %d'% (result.lenth, result.atleast))
    else:
        print('没有异常发生.')

if __name__ == '__main__':
    main()