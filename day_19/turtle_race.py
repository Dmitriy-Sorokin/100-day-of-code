import random
from turtle import Turtle, Screen

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-150, -100, -50, 0, 50, 100]
race_on = False
all_turtle = []

screen = Screen()
screen.setup(width=500, height=400)
user_be = screen.textinput(title="Make your bet", prompt="With turtle will win the race? Enter a color: ")

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(new_turtle)

if user_be:
    race_on = True

while race_on:

    for t in all_turtle:
        if t.xcor() > 230:
            race_on = False
            win_color = t.pencolor()
            if win_color == user_be:
                print(f"You won! The {win_color} turtle winner!")
            else:
                print(f"You lost! The {win_color} turtle winner!")

        rand_dist = random.randint(0, 10)
        t.forward(rand_dist)

screen.exitonclick()
