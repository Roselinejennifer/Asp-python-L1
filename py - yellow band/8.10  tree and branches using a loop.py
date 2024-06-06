import turtle

def draw_branch(branch_length, angle):
    if branch_length > 5:
        turtle.forward(branch_length)
        turtle.right(angle)
        draw_branch(branch_length - 15, angle)
        turtle.left(2 * angle)
        draw_branch(branch_length - 15, angle)
        turtle.right(angle)
        turtle.backward(branch_length)

def draw_tree(trunk_length, angle):
    turtle.left(90)
    turtle.penup()
    turtle.backward(trunk_length)
    turtle.pendown()
    draw_branch(trunk_length, angle)
    turtle.exitonclick()


turtle.setup(width=800, height=600)
turtle.speed(0)  # Set the speed of the turtle to the fastest


draw_tree(100, 30)

