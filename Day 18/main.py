import turtle
from turtle import *
from turtle import Turtle
import random


tim = Turtle()
tim.shape("turtle")
tim.color("dodger blue")

colors = ["dodger blue","red", "black", "green", "orange"]


for sides in range(3,10):
    angle = 360/sides
    for i in range(sides):
        tim.pencolor(random.choice(colors))
        tim.forward(100)
        tim.right(angle)



# for i in range(50):
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#     tim.forward(10)






screen = Screen()
screen.exitonclick()