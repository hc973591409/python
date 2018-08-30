# 4. 编写程序，完成“名片管理器”项目

# 需要完成的基本功能：
# 1. 进入系统，从文件读取
# 添加名片
# 删除名片
# 修改名片
# 查询名片
# 退出系统(写入文件)
# 程序运行后，除非选择退出系统，否则重复执行功能
# 导入自定义函数段

import fun_of_card as card

def main():
    card.init_card()
    while True:
        card.headers()
        op = input("请输入你的操作:")
        if op == '1':
            card.add_card()
        elif op == '2':
            card.delete_card()
        elif op == '3':
            card.change_card()
        elif op == '4':
            card.search_card()
        elif op == '5':
            card.write_2_file()
            exit()
        else:
            print("输入不正确，请重新输入")

if __name__ == '__main__':
    main()
    