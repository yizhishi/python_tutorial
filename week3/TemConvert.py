# temConvert
c = input("")
if c[-1] in ('F','f'):	#c[-1] 即可, 且c[len(c)-1:len(c)] 才是最后一位 
        output = (eval(c[0:-1]) - 32 ) / 1.8
        print(output) #保留2位不记得 print("{:.2f}".format(c))
elif c[-1:-2] in ('C', 'c'):
        output = (c[0:-1]) *1.8 + 32
        print(output) #保留2位不记得
else:
        print("格式错误")
