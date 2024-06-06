import turtle

#Get type of smile to draw
smile_type = input('What type of smiley do you want to draw (happy, sad, surprised)?')

#Initialize turtle
t = turtle.Turtle()

#Draw happy smile if smile type is happy
if smile_type == "happy":
    # Draw the head
    t.circle(50)
    # Draw the eyes
    t.penup()
    t.goto(-15, 60)
    t.pendown()
    t.circle(5)
    t.penup()
    t.goto(15, 60)
    t.pendown()
    t.circle(5)
    # Draw the mouth
    t.penup()
    t.goto(-25, 40)
    t.pendown()

    t.seth(-75)
    t.circle(25, 180)

#Draw happy sad if smile type is sad
elif smile_type == "sad":
    # Draw the head
    t.circle(50)
    # Draw the eyes
    t.penup()
    t.goto(-15, 60)
    t.pendown()
    t.circle(5)
    t.penup()
    t.goto(15, 60)
    t.pendown()
    t.circle(5)
    # Draw the mouth
    t.penup()
    t.goto(-15, 5)
    t.pendown()
    t.seth(-75)
    t.circle(20, -180)

#Draw happy surprised if smile type is surprised
elif smile_type == "surprised":
    # Draw the head
    t.circle(50)
    # Draw the eyes
    t.penup()
    t.goto(-15, 60)
    t.pendown()
    t.circle(5)
    t.penup()
    t.goto(15, 60)
    t.pendown()
    t.circle(5)
    # Draw the mouth
    t.penup()
    t.goto(0, 5)
    t.pendown()
    t.circle(20)

#If none of the above smile types are chosen print this statement
else:
    print("Invalid smiley type. Please choose either happy, sad, or surprised.")