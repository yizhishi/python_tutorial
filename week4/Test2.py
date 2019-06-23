# 100以内素数之和

'''
求100以内所有素数之和并输出。 ‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬
素数指从大于1，且仅能被1和自己整除的整数。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬

提示：可以逐一判断100以内每个数是否为素数，然后求和。
'''

result = 2
max = 100
for i in range(3 ,max):
    for j in range(2, i):
        if (i % j ==0):
            break
    else: # 利用了 for else语法,  for循环程序执行结束后进入else
        result += i

print(result)

# 是否素数
# 不是素数, 返回 -1
def isPrime(n):
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

# V2, use function
result = 0
for i in range(1, 101):
    if (isPrime(i)):
        result += i
print(result)


