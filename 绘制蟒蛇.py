# 绘制蟒蛇

import turtle  #引用函数库，另一种调用 form turtle import *

def drawSnake (rad,angle,len,neckrad):
    for i in range(len):
        turtle.circle(rad,angle)
        turtle.circle(-rad,angle)
    turtle.circle(rad,angle/2)
    turtle.fd(rad)
    turtle.circle(neckrad+1,180)
    turtle.fd(rad*2/3)

def main():
    turtle.setup(1400,1400,0,0)
    pythonsize=30
    turtle.pensize(pythonsize)
    turtle.pencolor("blue") 
    # turtle.pencolor("#3B9909")
    turtle.seth(-40)   # 小乌龟启动时的方向， 东是0，-40是逆时针-40°
    drawSnake(40,80,5,pythonsize/2)

main()
