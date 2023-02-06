import turtle

def draw_doraemon():
    # Create the turtle object
    t = turtle.Turtle()
    t.speed(0)

    # Draw the head
    t.penup()
    t.goto(-100,100)
    t.pendown()
    t.circle(100)

    # Draw the body
    t.penup()
    t.goto(-50,0)
    t.pendown()
    t.pensize(20)
    t.forward(100)
    t.pensize(1)

    # Draw the legs
    t.penup()
    t.goto(-75,-100)
    t.pendown()
    t.right(45)
    t.forward(70)
    t.right(90)
    t.forward(70)

    t.penup()
    t.goto(-25,-100)
    t.pendown()
    t.left(45)
    t.forward(70)
    t.left(90)
    t.forward(70)

    # Draw the arms
    t.penup()
    t.goto(-50,50)
    t.pendown()
    t.right(135)
    t.forward(70)
    t.right(90)
    t.forward(70)

    t.penup()
    t.goto(-50,-50)
    t.pendown()
    t.left(135)
    t.forward(70)
    t.left(90)
    t.forward(70)

    # Draw the eyes
    t.penup()
    t.goto(-60,120)
    t.pendown()
    t.circle(10)

    t.penup()
    t.goto(-40,120)
    t.pendown()
    t.circle(10)

    # Draw the mouth
    t.penup()
    t.goto(-50,80)
    t.pendown()
    t.right(135)
    t.forward(30)
    t.left(90)
    t.forward(30)

    turtle.done()

# Call the function to draw Doraemon
draw_doraemon()
