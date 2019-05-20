#DayDayUp.py

#Q1
dayUp = pow(1.001, 365)
dayDown = pow(0.999, 365) 
print("向上: {:2f}, 向下: {:.2f}".format(dayUp, dayDown)) #print 时的 format

#Q2

year = 365
def day(base, factor):
    return round(base ** factor, 2)


#print(day(1.001, year)) #Q1
#print(day(0.009, year)) #Q1
print(day(1+ 0.005, year))
print(day(1- 0.005, year))


#Q3
'''
365天, 工作日进步1%, 休息日退步1%
'''
base =1
factor = 0.01

for i in range(365):
    if (i %7 in [6, 0]):
        #print("before%f" %base)
        base = base * (1 - factor)
        #print("after%f" %base)
    else:
        base = base * (1 + factor)

print(base)

#Q4
def dayUp(df):
    dayUp = 1
    for i in range(365):
        if i %7 in [6, 0]:
            dayUp = dayUp * (1- 0.01)
        else:
            dayUp = dayUp * (1 + df)
    return dayUp

df = 0.01
while dayUp(df) < 37.78:
    df += 0.001
print('df: {:.3f}'.format(df))
