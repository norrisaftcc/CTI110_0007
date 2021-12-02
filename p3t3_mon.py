# CTI 110
# P3T3 - Turtles
# Name
# Date

import turtle # required to use turtle graphics
# forward, left, and right 

# setup - size, color, etc.
turtle.pensize(3)
turtle.pencolor("green")
turtle.shape("turtle")
turtle.speed(2)

# draw a rectangle

turtle.forward(100)
turtle.left(90)

# shortcuts - fd() is forward, lt() and rt() are left/right
turtle.fd(100)
turtle.lt(90)
turtle.fd(100)
turtle.lt(90)
turtle.fd(100)

# move away so we can draw another shape
turtle.penup()
turtle.forward(50)
turtle.pendown()

# draw a triangle
# angle is 360 / number of sides
turtle.pencolor("blue")
turtle.forward(80)
turtle.right(120)
turtle.forward(80)
turtle.right(120)
turtle.forward(80)

# prints text at turtle location
turtle.pencolor("red")

turtle.write("Hello, World") 



