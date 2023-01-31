from turtle import Turtle, Screen

timmi = Turtle()

timmi.shape("turtle")
timmi.color("red")
# for _ in range(4):
#     timmi.forward(100)
#     timmi.right(90)
#     timmi.pendown()
#     timmi.penup()

for _ in range(15):
    timmi.forward(10)
    timmi.penup()
    timmi.forward(10)
    timmi.pendown()

screen = Screen()
screen.exitonclick()

'''Ромб имеет угл 72 градуса'''