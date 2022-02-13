from turtle import Turtle, Screen, colormode
import random


sam = Turtle()
colormode(255)
sam.pensize(10)
sam.speed(15)
for i in range(200):
    x = random.randint(0,255)
    y = random.randint(0, 255)
    z = random.randint(0, 255)
    sam.pencolor(x, y, z)
    direction = random.randint(0,3)
    if direction == 1:
        sam.left(90)
    elif direction == 2:
        sam.left(90)
        sam.left(90)
    elif direction == 0:
        sam.right(90)
    sam.forward(30)


screen = Screen()
screen.exitonclick()