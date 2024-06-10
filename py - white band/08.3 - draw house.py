import turtle
screen = turtle.Screen()
screen.bgcolor("sky blue")
house = turtle.Turtle()
house.speed(2)
def draw_rectangle(t, width, height, color):
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()
def draw_triangle(t, length, color):
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(3):
        t.forward(length)
        t.left(120)
    t.end_fill()
def draw_house():
    house.penup()
    house.goto(-50, -50)
    house.pendown()
    draw_rectangle(house, 100, 100, "lightgrey")
    house.penup()
    house.goto(-50, 50)
    house.pendown()
    draw_triangle(house, 100, "brown")
    house.penup()
    house.goto(-15, -50)
    house.pendown()
    draw_rectangle(house, 30, 50, "red")
draw_house()
house.hideturtle()
turtle.done()