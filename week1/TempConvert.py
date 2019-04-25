#TempConvert.py
'''


空白行也是程序的一部分
'''
Temp = input("输入温度(以F或C结尾): ")
while True:
    if len(Temp) <= 0:
        Temp = input("输入温度(以F或C结尾): ")
    else:
        break
print("输入的数值是: {}".format(eval(Temp[0:-1])))
if Temp[-1] in ['f', 'F']:      #[-1] 从右开始
    C = (eval(Temp[0: -1]) - 32)/1.8      #eval('print("hello")')
    print("温度是: {:.2f}C".format(C))
elif Temp[-1] in ['C', 'c']:
    F = 1.8 * eval(Temp[0: -1]) + 32
    print("温度是: {:.2f}F".format(F))
else:
    print("输入格式错误")
