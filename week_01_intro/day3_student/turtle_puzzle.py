# turtle_puzzle_house.py

import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("skyblue")
screen.title("Turtle House – No Loops!")

# Create the turtle
builder = turtle.Turtle()
builder.pensize(3)
builder.speed(3)

# Draw the house base
builder.color("black", "burlywood")  # outline, fill
builder.begin_fill()
builder.forward(150)
builder.left(90)
builder.forward(100)
builder.left(90)
builder.forward(150)
builder.left(90)
builder.forward(100)
builder.end_fill()

# Move to roof position
builder.penup()
builder.left(90)
builder.forward(150)
builder.left(90)
builder.pendown()

# Draw the roof (triangle)
builder.color("black", "darkred")
builder.begin_fill()
builder.right(45)
builder.forward(106)  # approx length of diagonal
builder.right(90)
builder.forward(106)
builder.end_fill()

# Move to door position
builder.penup()
builder.left(135)
builder.forward(60)
builder.right(90)
builder.forward(100)
builder.pendown()

# Draw the door
builder.color("black", "saddlebrown")
builder.begin_fill()
builder.right(90)
builder.forward(40)
builder.left(90)
builder.forward(60)
builder.left(90)
builder.forward(40)
builder.end_fill()

# Done!
builder.hideturtle()
screen.exitonclick()
