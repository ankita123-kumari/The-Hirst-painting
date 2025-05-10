
import turtle
import random

# Set up the screen for full size
screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)  # Makes the window fullscreen
turtle.colormode(255)
t = turtle.Turtle()
t.speed("fastest")
t.penup()
t.hideturtle()

# Define colors
colors = [(234, 72, 53), (247, 221, 89), (77, 177, 233), (186, 92, 219), 
          (66, 227, 138), (245, 129, 53), (239, 77, 118), (143, 69, 216)]

# Adjust dot positioning for full screen
dot_size = 30  # Increase dot size for better visibility
spacing = 50   # Adjust spacing between dots
rows = 15      # Increase row count
cols = 15      # Increase column count

# Position the turtle
start_x = -((cols - 1) * spacing) // 2
start_y = -((rows - 1) * spacing) // 2
t.goto(start_x, start_y)

# Draw dots across the screen
for row in range(rows):
    for col in range(cols):
        t.dot(dot_size, random.choice(colors))
        t.forward(spacing)
    t.goto(start_x, t.ycor() + spacing)

# Exit on click
screen.exitonclick()



