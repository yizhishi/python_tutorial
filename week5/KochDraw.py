# KochDraw.py
'''
       ↗↘
----         ----
'''
# 科赫曲线
import turtle

def koch(size, n):
    if ( n == 0):
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]: # turtle 左转的角度 0, 60, -120, 60
            turtle.left(angle)
            koch(size / 3, n - 1)

def main():
    turtle.setup(1400, 800, 20, 20)
    turtle.penup()
    turtle.goto(-300, 100)
    turtle.pendown()
    turtle.pensize(2)

    level = 3

    koch(400, level) # 3条科赫曲线 连成一个科赫雪花
    turtle.right(120)
    koch(400, level)
    turtle.right(120)
    koch(400, level)
    turtle.right(120)
    
    turtle.hideturtle()

main()


