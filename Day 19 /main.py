import turtle
from turtle import *
screen = Screen()
screen.setup(width = 500,height=400)
user_bets = screen.textinput(title="Make your bet", prompt="Which turtle will win the race")
colors = ["red","orange","yellow","green","blue","purple"]
y_positions = [-70,-40,-10,20,50,80]

for turtle_index in range(0,6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(x=-230,y =y_positions[turtle_index])


















screen.exitonclick()






