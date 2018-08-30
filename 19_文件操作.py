# r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
# w	打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
# wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# r+	打开一个文件用于读写。文件指针将会放在文件的开头。
# w+	打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
# rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
# wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
# f.write() 写入文件
# f.read() 从文件读取
# f.readlines() 文件全部读取，按行存储，返回一个列表
# f.readline() 读取一行，文件指针到下一行开头

str1 = '''# r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
    # w	打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
    # a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
    # rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
    # wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
    # ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
    # r+	打开一个文件用于读写。文件指针将会放在文件的开头。
    # w+	打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
    # a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
    # rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
    # wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
    # ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
    # f.write() 写入文件
    # f.read() 从文件读取
    # f.readlines() 文件全部读取，按行存储，返回一个列表
    # f.readline() 读取一行，文件指针到下一行开头'''

def write_to_file():
    f = open('text.txt','w')
    f.write(str1)
    f.close()

# 读取文件 拷贝文件
def copy_to_file():
    oldfile = input("请输入要拷贝的文件:")
    # text.txt
   
    flag = oldfile.rfind('.')
    newfile = oldfile[:flag]+'[附件]'+oldfile[flag:]
    # print(newfile)
    fread = open(oldfile)
    new_str = fread.readlines()
    fwrite = open(newfile,'w')
    for i in new_str:
        fwrite.write(i)
    fread.close()
    fwrite.close()

# 移动文件指针
def file_tell():
    f = open('text.txt')
    str1 = f.read(20)
    print(str1)
    # 获取当前文件位置
    print(f.tell())

    # seek(offset, from)有2个参数
    # offset:偏移量
    # from:方向
        # 0:表示文件开头
        # 1:表示当前位置
        # 2:表示文件末尾
    f.seek(0,1)
    str2 = f.readline()
    print(str2)
    f.close()


import os
# 文件重命名
def file_rename():
    # os.rename('text.txt','text.py')
    # 删除文件
    os.remove('text[附件].txt')


# 文件夹的相关操作
def folder():
    # 创建文件夹
    # os.mkdir("folder")
    # 获取当前路径
    print(os.getcwd())
    os.chdir('../')
    print(os.listdir())
    os.chdir('./python')
    os.rmdir('folder')


# 批量重命名
def file_renames():
    # 进入需要重命名的文件夹
    os.chdir('../list')
    print(os.listdir())
    for filename in os.listdir():
        os.rename(filename, '[超哥出品]'+filename)

# 读取一个文件，去掉#读取
def comment():
    # 因为编码格式有问题，要指定解码格式为utf8，windows都是gbk编码
    f = open('01.py','r',encoding='utf-8')
    for line in f.readlines():
        if line.startswith('#'):
            continue
        print(line)

def main():
    # copy_to_file()
    comment()


if __name__ == '__main__':
    main()