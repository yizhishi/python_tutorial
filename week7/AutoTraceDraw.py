#AutoTraceDraw.py

import turtle

def initPen():
    turtle.title('轨迹绘制')
    turtle.setup(800, 600, 0, 0)
    turtle.pencolor('red')
    turtle.pensize(5)


def getData():
    f = open('data.txt')
    dataList = []
    for line in f.readlines():
        line = line.replace('\n', '')
        dataList.append(list(map(eval, line.split(','))))
    else:
        f.close()
        return dataList


def draw(data):
    for i in range(len(data)):
        turtle.pencolor(data[i][-3], data[i][-2], data[i][-1])
        turtle.fd(data[i][0])
        if data[i][1]  :
            turtle.right(data[i][2])
        else:
            turtle.left(data[i][2])


def main():
    initPen()
    #print (getData())
    draw(getData())
    turtle.down()

main()
