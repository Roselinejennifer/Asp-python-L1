from turtle import *

step = 6

speed(75)

for i in range(180):
    for j in range(16):
        forward(0.5 * i + j)
        left(77 / step)  # The golden ratio
        hideturtle()
        color("black")
        pensize(2)  # Eventually change to smaller or big if.

    left(77)