#String

str='0123456789'

# 前包括, 后不包括
print(str[2:]) # 对字符切片, 从下标为2至结束, 23456789

print(str[:6]) # 切片, 从开始至下标为6, 012345

print(str[2:6]) # 切片, 从下标为2至下标为6,  2345

print(str[1:8:2]) # 切片, 从下标为1开始至下标为8 步长为2, 1357

print(str[::-1]) # 逆序, 从开始至结尾 步长为-1

print('\b')
