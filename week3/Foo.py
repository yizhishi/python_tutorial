#Foo.py

print(0.2+0.1)
print(round(0.2+0.1,2))


#复数
z=1.23e-4 + 5.6e+89j #复数, python 大法好
print(z)
#print(round(z,6)) # TypeError: type complex doesn't define __round__ method
print(z.real) 
print(z.imag)


print(10 / 2) # 浮点
print(10 // 3) # 整除
print( 2 ** 3) #power
print( 2 ** 0.5)#power


print(abs(-1.3)) #1.3 绝对值
print(divmod(10,3)) #divide mod 商余  (x//y, x%y) 结果是(3, 1)
print(pow(2,4,5)) # 幂余 2^4 / 5
print(max(1,-10,0)) # min(int ...)
print(int(0.2+0.1))
print(int("1"))# float(x) complex(x)
