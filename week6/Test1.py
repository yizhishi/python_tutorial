#Test1.py
'''
获得用户输入的一个整数N，输出N中所出现不同数字的和。
例如：用户输入 123123123，其中所出现的不同数字为：1、2、3，这几个数字和为6。
'''


num = input()
s = set()
result = 0

for i in num:
    s.add(eval(i))

for i in s:
    result +=i

print(result)
