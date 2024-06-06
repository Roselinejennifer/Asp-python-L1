import turtle
turtle.showturtle()
turtle.shape("turtle")
turtle.pencolor('red')
for x in range(20):
    turtle.forward(100)
    if x % 2 ==0:
        turtle.left(175)
    else:
        turtle.left(225)
turtle.done()