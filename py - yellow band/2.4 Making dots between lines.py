from turtle import *

step = 6 #Change its values as much as you'd like to
speed(50)
for i in range(400): #Eventually 360 is better sometimes
    forward(i * 3/step + i)
    left(400/step + 0.350)
    hideturtle()
    dot(20)
    pensize(2)