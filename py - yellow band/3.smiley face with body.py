import turtle
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Smiley Face with Body")
smiley = turtle.Turtle()
smiley.penup()
smiley.goto(0, -100)
smiley.pendown()
smiley.color("yellow")
smiley.begin_fill()
smiley.circle(100)
smiley.end_fill()

smiley.penup()
smiley.goto(-35, 35)
smiley.pendown()
smiley.color("black")
smiley.begin_fill()
smiley.circle(10)
smiley.end_fill()


smiley.penup()
smiley.goto(35, 35)
smiley.pendown()
smiley.color("black")
smiley.begin_fill()
smiley.circle(10)
smiley.end_fill()

smiley.penup()
smiley.goto(-40, -10)
smiley.setheading(-60)
smiley.width(5)
smiley.pendown()
smiley.circle(50, 120)

body = turtle.Turtle()


body.penup()
body.goto(-50, -100)
body.pendown()
body.color("blue")
body.begin_fill()
for _ in range(2):
    body.forward(100)
    body.right(90)
    body.forward(150)
    body.right(90)
body.end_fill()


body.penup()
body.goto(-50, -50)
body.pendown()
body.width(10)
body.goto(-100, -50)

body.penup()
body.goto(50, -50)
body.pendown()
body.goto(100, -50)

body.penup()
body.goto(-30, -250)
body.pendown()
body.goto(-30, -300)

body.penup()
body.goto(30, -250)
body.pendown()
body.goto(30, -300)

smiley.hideturtle()
body.hideturtle()

turtle.done()