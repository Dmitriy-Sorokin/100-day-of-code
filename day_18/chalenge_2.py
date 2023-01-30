import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    r_c = (r, g, b)
    return r_c

n_l = [0, 90, 180, 270]

random_side = random.choice(n_l)
tim.speed(10)

score = 0
while score < 50:
    score += 1
    random_side = random.choice(n_l)
    tim.forward(30)
    tim.setheading(random_side)
    tim.pensize(10)
    tim.pencolor(random_color())
