import turtle
from turtle import *
from turtle import Turtle
import random
turtle.colormode(255)

tim = Turtle()
tim.shape("turtle")
tim.color("dodger blue")




def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0,255)

    return(r,g,b)




# for sides in range(3,10):
#     angle = 360/sides
#     for i in range(sides):
#         tim.pencolor(colors)
#         tim.forward(100)
#         tim.right(angle)



# for i in range(50):
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#     tim.forward(10)







# def random_walk():
#     angle = random.uniform(0, 360)
#     tim.pencolor(random_color())
#     tim.forward(10)
#     tim.right(angle)
#
# for _ in range(200):
#     random_walk()



tim.circle(50,360,50,)
tim.right(1)
tim.circle(50,360, 50,)
tim.right(2)
tim.circle(50,360,50,)




screen = Screen()
screen.exitonclick()