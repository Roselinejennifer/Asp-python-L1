import turtle
angle=91
turtle.showturtle()
turtle.shape("turtle")
turtle.speed(0)
for x in range(100):
    turtle.circle(x)
    turtle.left(angle)
turtle.done()