from turtle import Turtle, Screen

tim = Turtle()
tim.pensize(5)

def move():
    tim.forward(10)


def right():
    tim.right(10)


def left():
    tim.left(10)


def clear():
    tim.clear()
    tim.penup()
    tim.sety(0)
    tim.setx(0)
    tim.pendown()


screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move)
screen.onkey(key="d", fun=right)
screen.onkey(key="a", fun=left)
screen.onkey(key="space", fun=clear)
screen.exitonclick()
