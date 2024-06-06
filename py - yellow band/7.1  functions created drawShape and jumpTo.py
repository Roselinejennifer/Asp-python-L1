import turtle

t=turtle.Turtle()

def drawShape(color, shape, length, angle):
    t.begin_fill()
    t.fillcolor(color)
    for i in range(shape):
        t.forward(length)
        t.left(angle)
    t.end_fill()

def jumpTo(x, y):
    t.penup()
    t.goto(x,y)
    t.pendown()


# t.begin_fill()
# t.fillcolor("red")
# for i in range(8):
#     t.forward(50)
#     t.left(45)
# t.end_fill()
drawShape("red", 8, 50, 45)


# t.penup()
# t.goto(-142,25)
# t.pendown()
jumpTo(-142,25)

# t.begin_fill()
# t.fillcolor("green")
# for i in range(6):
#     t.forward(50)
#     t.left(60)
# t.end_fill()
drawShape("green", 6, 50, 60)

# t.penup()
# t.goto(142,25)
# t.pendown()
jumpTo(142,25)

# t.begin_fill()
# t.fillcolor("blue")
# for i in range(7):
#     t.forward(50)
#     t.left(52)
# t.end_fill()
drawShape("blue", 7, 50, 52)

# t.penup()
# t.goto(142,-155)
# t.pendown()
jumpTo(142,-155)

# t.begin_fill()
# t.fillcolor("yellow")
# for i in range(11):
#     t.forward(50)
#     t.left(32)
# t.end_fill()
drawShape("yellow", 11, 50, 32)

# t.penup()
# t.goto(-142,-155)
# t.pendown()
jumpTo(-142,-155)

# t.begin_fill()
# t.fillcolor("purple")
# for i in range(10):
#     t.forward(50)
#     t.left(37)
# t.end_fill()
drawShape("purple", 10, 50, 37)


# t.penup()
# t.goto(0,-250)
# t.pendown()
jumpTo(0,-250)


# t.begin_fill()
# t.fillcolor("pink")
# for i in range(9):
#     t.forward(50)
#     t.left(41)
# t.end_fill()
drawShape("pink", 9, 50, 41)
