# SevenDigitsDraw.py
import turtle
import time

# 
def drawGap():
    turtle.penup()
    turtle.fd(5)
    
# 画七段数码管的一段
def drawLine(isDraw):
    drawGap()
    turtle.pendown() if isDraw else turtle.penup()
    turtle.fd(40)
    drawGap
    turtle.right(90)
    
# 画数字
def drawDigit(digit):

    # 下半部分绘制
    drawLine(False) if digit in [0, 1, 7] else drawLine(True)
    drawLine(False) if digit in [2] else drawLine(True)
    drawLine(False) if digit in [1, 4, 7] else drawLine(True)
    drawLine(False) if digit in [1, 3, 4, 5, 7, 9] else drawLine(True)

    turtle.left(90)

    # 上半部分绘制
    drawLine(False) if digit in [1, 2, 3, 7] else drawLine(True)
    drawLine(False) if digit in [1, 4] else drawLine(True)
    drawLine(False) if digit in [5, 6] else drawLine(True)

    turtle.left(180)
    turtle.penup()
    turtle.fd(40)


# 
def drawDate(date):
    year = date[0: 4]
    month = date[4: 6]
    day = date[-2:]
    for i in year:
        i = eval(i)
        turtle.pencolor('red')
        drawDigit(i)
        turtle.fd(40)
    for i in month:
        i = eval(i)
        turtle.pencolor('green')
        drawDigit(i)
        turtle.fd(40)
    for i in day:
        i = eval(i)
        turtle.pencolor('blue')
        drawDigit(i)    

def main():
    # 当前年月日
    date = time.strftime('%Y%m%d', time.gmtime())

    turtle.setup(1000, 400, 200, 200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    
    drawDate(date)
    
    turtle.hideturtle()
    turtle.done()


main()

 
