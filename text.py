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