card_list = []

def init_card():
    try:
        with open('card.txt','r') as f:
            card_list.extend(eval(f.read()))
            # print(card_list) eval的作用相当于去掉字符串的'' 转为表达式         
    except:
        pass
    

def headers():
    print('*'*50)
    print("1.添加名片")
    print("2.删除名片")
    print("3.修改名片")
    print("4.查询名片")
    print("5.退出系统(写入文件)")
    print('*'*50)

# 姓名  电话  qq 地址
def table_head():
    print('='*50)
    print("姓 名:\t电 话:\tQQ:\t地 址:\t\t")
    print('-'*50)

def add_card():
    name = input("请输入姓名:")
    phone = input("请输入电话:")
    QQ = input("请输入qq:")
    address = input("请输入地址:")
    card = {}
    card['name'] = name
    card['phone'] = phone
    card['QQ'] = QQ
    card['address'] = address
    card_list.append(card)

def search_card():
    table_head()
    # print(card_list)
    for i in card_list:
        print(i['name'],end = '\t')
        print(i['phone'],end = '\t')
        print(i['QQ'],end = '\t')
        print(i['address'],end = '\t')
        print('')
    
def write_2_file():
    with open("card.txt",'w') as f:
        f.write(str(card_list))

def delete_card():
    name = input("请输入你要删除的名片名字：")
    # [{'name': '23', 'phone': 'asdf', 'QQ': 'dfg', 'address': '3t'},
    #  {'name': 'ag', 'phone': 'sdg', 'QQ': 'gsdf', 'address': '2354'}]
    j = 0
    for i in card_list:
        if i['name'] ==  name:
            break
        j += 1
    if j < len(card_list):
        del card_list[j]


def change_card():
    name = input("请输入你要修改的名片名字：")
    card = {}
    j = 0
    for i in card_list:
        if i['name'] ==  name:
            phone = input("请输入你要修改的名片电话（直接回车不修改）：")
            card['name'] = i['name']
            if phone:
                card['phone'] = phone
            else:
                card['phone'] = i['phone']

            QQ = input("请输入你要修改的名片QQ（直接回车不修改）：")
            if QQ:
                card['QQ'] = QQ
            else:
                card['QQ'] = i['QQ']

            address = input("请输入你要修改的名片地址（直接回车不修改）：")
            if address:
                card['address'] = address
            else:
                card['address'] = i['address']
            break
        j += 1
        print(card)
    card_list[j] = card

    if j >= len(card_list):
        print("没有找到需要修改的名片")