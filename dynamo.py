import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=400)
screen.bgcolor("white")
screen.title("Display DYNAMO")

# Create a turtle object
t = turtle.Turtle()
t.hideturtle()
t.penup()
t.speed("fastest")

# Set the font style
font = ("Arial", 48, "bold")

# Write "DYNAMO" on the screen
t.goto(0, 0)  # Position the turtle at the center
t.write("DYNAMO", align="center", font=font)

# Exit on click
screen.exitonclick()