from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.move_speed = 0.2

    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def start_p(self):
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def m_speed(self):
        self.move_speed *= 0.7
