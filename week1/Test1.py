'''
获得用户输入的一个整数，参考该整数值，打印输出"Hello World"，要求：‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬

如果输入值是0，直接输出"Hello World"‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬

如果输入值大于0，以两个字符一行方式输出"Hello World"（空格也是字符）‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬

如果输入值小于0，以垂直方式输出"Hello World"
'''
output = "Hello World"
inputStr = input("")

inputInt = eval(inputStr)
if inputInt == 0 :
    print("Hello World")
elif inputInt > 0:
    for n in range(len(output)):
        if n + 1 < len(output) and (n % 2) != 0:
            print(output[n - 1] + output[n])
        if n + 1 == len(output) and (n % 2) == 0:
            print(output[n] )
        if n + 1 == len(output) and (n % 2) != 0:
            print(output[n - 1] + output[n])
else:
    for n in range(len(output)):
        print(output[n])
 
