#WeekNamePrint.py

#V1
weekStr='星期一星期二星期三星期四星期五星期六星期天'
weekId =eval(input('输入星期数字1~ 7: '))
pos = (weekId - 1 ) * 3
print(weekStr[pos: pos+3])

#V2
weekStr = '一二三四五六日'
weekId = eval(input('输入数字1~7: '))
pos = (weekId - 1)
print('星期' + weekStr[pos: pos +1])

print(ord('关'))
#输出十二星座
for i in range(12): 
    print(chr(9800+i), end = '') #end = '' 输入不换行
    

