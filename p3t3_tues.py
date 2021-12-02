# CTI 110
# P3T3
# Name
# Date

# we use import to activate the turtle
import turtle

# optional (you can skip these)
turtle.pensize(2)
turtle.pencolor("red")
turtle.speed(1)

# forward, right, and left
# rectangle start
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
# rectangle end

# other shapes can be made --
# the turn angle is 360/numSides.
# (example: rectangles are 90, triangles are 120)

turtle.penup()
turtle.forward(100)
turtle.pendown()
turtle.pencolor("blue")
turtle.forward(50)
turtle.left(120)
turtle.forward(50)
turtle.left(120)
turtle.forward(50)
turtle.left(120)

# write() will print text
turtle.pencolor("green")
turtle.write("Hello world")
