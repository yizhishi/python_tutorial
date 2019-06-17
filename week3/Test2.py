# Test2
'''
获得输入的一个字符串s，以字符减号(-)分割s，将其中首尾两段用加号(+)组合后输出。
Alice-Bob-Charis-David-Eric-Flurry    Alice+Flurry
'''

inputStr = input('')
str = inputStr.split('-')
print('{}+{}'.format(str[0],str[-1]))
