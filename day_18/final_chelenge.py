import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()
turtle.colormode(255)
tim.hideturtle()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    r_c = (r, g, b)
    return r_c


def forward():
    tim.penup()
    for _ in range(10):
        tim.dot(20, random_color())
        tim.forward(50)


def cordinate(cord):
    tim.penup()
    tim.setx(0)
    return tim.sety(cord)


cordin = 0
for _ in range(10):
    cordin += 40
    cordinate(cordin)
    forward()

screen = Screen()
screen.exitonclick()
