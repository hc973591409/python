# python os.path模块比较实用的函数介绍
# Python os模块包含普遍的操作系统功能。如果你希望你的程序能够与平台无关的话，这个模块是尤为重要的。(一语中的)
# 常用方法
import os
# 输出字符串指示正在使用的平台。如果是window 则用’nt’表示，对于Linux/Unix用户，它是’posix’。
print(os.name)
# 函数得到当前工作目录，即当前Python脚本工作的目录路径。
print(os.getcwd())
# 返回指定目录下的所有文件和目录名。
# print(os.listdir())
# 删除一个文件。
# os.remove('1.txt')
# os.system('dir')    # 相当于用cmd执行dir命令
# os.system('cmd')  
# print(os.sep('#'))
# os.path.isdir 判断是不是目录
print(os.path.isdir(os.getcwd()))
print(os.path.isdir('01.py'))
# os.path.exists()函数用来检验给出的路径是否真地存在
print(os.path.exists("C:\\Users\\97359\\"))
print(os.path.abspath('./'))
print(os.path.getsize('01.py')) # 获得文件大小，如果name是目录返回0L
# os.path.splitext():分离文件名与扩展名
print(os.path.splitext('a.txt') )
print(os.path.join('./','a.txt'))
print(os.path.join('c:\Python','f1') )
print(os.path.basename('c:\Python\a.txt') )