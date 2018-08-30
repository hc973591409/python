# int(x [,base ])	将x转换为一个整数
str1 = '100'
print(int(str1,base=8)) # 转为八进制
print(int(str1))       #不写参数默认为10进制
# python基本不用long类型
# long(x [,base ])	将x转换为一个长整数
str1 = '100.1'
print(float(str1))
# float(x )	将x转换到一个浮点数
# complex(real [,imag ])	创建一个复数
# str(x )	将对象 x 转换为字符串
# repr(x )	将对象 x 转换为表达式字符串
# eval(str )	用来计算在字符串中的有效Python表达式,并返回一个对象  相当于把字符串的引号去掉了
# tuple(s )	将序列 s 转换为一个元组
# list(s )	将序列 s 转换为一个列表
# chr(x )	将一个整数转换为一个字符
# unichr(x )	将一个整数转换为Unicode字符
# ord(x )	将一个字符转换为将一个字符转换为它的整数值
# hex(x )	将一个整数转换为一个十六进制字符串
# oct(x )	将一个整数转换为一个八进制字符串

# 简单的选择嵌套
def compile(username, userpasswd):
    local_name = 'huchao'
    local_passwd = '123456'
    if username == local_name:
        print("用户名正确")
        if local_passwd == userpasswd:
            print("欢迎登陆爱学习系统：")
        else:
            print("对不起密码错误")

    else:
        print("用户名错误")

def main():
    print("*"*50)
    user_name = input("请输入用户名：")
    user_passwd = input("请输入密码：")
    compile(user_name,user_passwd)
    print("*"*50)

if __name__ == '__main__':
    main()