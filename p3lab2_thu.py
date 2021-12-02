# CTI 110
# P3LAB2
# Name
# Date

# Some turtle graphics

# Part 1 - draw a triangle and a square.
import turtle
t = turtle.Turtle()    # make a new turtle and name it

# Set pen color, size, speed if you like.
t.pencolor("green") # "blue", "red", etc.
t.pensize(2)
t.speed(2)  # 1 - 10, 1 is slowest (0 is instant)

# In general, a polygon is 360 degrees, divided by # of sides.


# Draw a triangle
t.pencolor("#66ffff") # light blue i guess
for side in [1, 2, 3]:
    t.forward(100)
    t.right(120)

# Draw a square
t.pencolor("#0000FF")
for side in [1, 2, 3, 4]:
    t.forward(100)
    t.left(90)



# Part 2 - draw your initials
t.pencolor("red")
# Letter #1 - "A"
t.left(70)
t.forward(40)
t.right(90)
t.forward(30)
t.backward(30)
t.left(90)
t.forward(40)
t.right(150)
t.forward(80)



# Space
t.left(80)
t.penup()
t.forward(100)
t.pendown()

# Letter #2
# Letter "T"
t.left(90)
t.forward(80)
t.right(90)
t.forward(30)
t.backward(60)

# Space
t.penup()
t.forward(150)
t.pendown()

# Letter #3
# "C"
t.forward(60)
t.backward(60)
t.right(90)
t.forward(80)
t.left(90)
t.forward(60)





# Part 3 - Bonus
