import turtle

t=turtle.Turtle()

t.begin_fill()
t.fillcolor("red")
for i in range(8):
    t.forward(50)
    t.left(45)
t.end_fill()

t.penup()
t.goto(-142,25)
t.pendown()
t.begin_fill()
t.fillcolor("green")
for i in range(6):
    t.forward(50)
    t.left(60)
t.end_fill()

t.penup()
t.goto(142,25)
t.pendown()
t.begin_fill()
t.fillcolor("blue")
for i in range(7):
    t.forward(50)
    t.left(52)
t.end_fill()


t.penup()
t.goto(142,-155)
t.pendown()
t.begin_fill()
t.fillcolor("yellow")
for i in range(11):
    t.forward(50)
    t.left(32)
t.end_fill()


t.penup()
t.goto(-142,-155)
t.pendown()
t.begin_fill()
t.fillcolor("purple")
for i in range(10):
    t.forward(50)
    t.left(37)
t.end_fill()
t.penup()
t.goto(0,-250)
t.pendown()
t.begin_fill()
t.fillcolor("pink")
for i in range(9):
    t.forward(50)
    t.left(41)
t.end_fill()



