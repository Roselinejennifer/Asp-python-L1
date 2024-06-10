from turtle import *

step = 6 
speed(50)
for i in range(400):
    forward(i * 3/step + i)
    left(400/step + 0.350)
    hideturtle()
    dot(20)
    pensize(2)
