import turtle



# Define the custom functions

def square(size):

    for i in range(4):

        turtle.forward(size)

        turtle.left(90)



def triangle(size):

    for i in range(3):

        turtle.forward(size)

        turtle.left(120)



# Use the custom functions to draw shapes

turtle.speed(1)

turtle.color("blue")



square(100)

turtle.penup()

turtle.forward(150)

turtle.pendown()



triangle(100)



turtle.done()

