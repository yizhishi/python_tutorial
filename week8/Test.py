#Test.py
'''
test1
获得用户的任何可能输入，将其中的英文字符进行打印输出，程序不出现错误。
*&^123abc0e abce
'''

'''
import re

str=input()
res = ''.join(re.findall(r'[A-Za-z]', str)) 
print(res)
'''

'''
test2
获得用户输入的一个数字，可能是浮点数或复数，如果是整数仅接收十进制形式，且只能是数字。
对输入数字进行平方运算，输出结果。
'''

x = input()
try:
    y = eval(x)
    if isinstance(y, complex) or isinstance(y, float):
        print(y ** 2)
    elif x.isdigit():
         print(y ** 2)
    else:
        print('输入有误')        
except:
    print('输入有误')
