#PythonDraw.py
import turtle as t
t.setup(650, 350, 200, 200)
t.penup()
t.fd(-250)  # 后退
t.pendown()
t.pensize(25) # t.width(25)
#t.pencolor('purple')
t.pencolor(0.63, 0.13, 0.94)  # t.pencolor((0.63, 0.13, 0.94))
t.seth(-40) # 角度 turtle.setheading(angle)   turtle.left(angle)   turtle.right(angle)
for i in range(4): # 老是忘记for和if后边的 : 
    t.circle(40, 80)
    t.circle(-40, 80) # turtle.circle(r, extend=None) 
t.circle(40, 80/2)
t.fd(40)
t.circle(16,180)
t.fd(40 * 2 / 3)
t.done() # 不自动退出

#   amazing
