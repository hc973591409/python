# 字符串切片
string = 'abcdefgh'
# 取索引值0，1，2，包含头，不包含尾
print(string[0:3])
print(string[0:3])
# 从索引值一直取到最后
print(string[2:])
# 取 下标为1开始 到 最后第2个  之间的字符
print(string[1:-1])

# （面试题）给定一个字符串aStr, 请反转字符串
print(string[-1::-1])