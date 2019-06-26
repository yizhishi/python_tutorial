# Test2.py
'''
获得用户输入数字N，计算并输出从N开始的5个质数，单行输出，质数间用逗号,分割。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬

注意：用户输入的数字N可能是浮点数，都是正数；最后一个输出后不用逗号。
'''
# 请在...补充一行或多行代码

def prime(m):
    if (n < 2):
        return False
    elif ( n == 2):
        return True
    elif (n % 2 ==0):
        return False
    else:
        for i in range(2, n):
            if (n % i ==0):
                return False
        else:
            return True

n = eval(input())
if (isinstance(n, int) == False): # 处理输入
    n = int(n)
if (n <= 0):
    n = 1

count = 0 # 计数
result = [] # 结果
while ( count < 5 ):
#    print('count: {}, n: {}'.format(count, n))
    if prime(n) :
        result.append(n)
        count +=1
    n += 1


for i in result: # 打印
    if ( i == result[len(result)-1] ):
        print(i, end = "")
    else:
        print(i, end = ",")
        

