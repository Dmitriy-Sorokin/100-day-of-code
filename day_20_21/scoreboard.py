from turtle import Turtle, Screen

ALIGNMENT = "center"
FONT = ('Arial', 18, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.shape()
        self.penup()
        self.pencolor("white")
        self.speed(100)
        self.goto(0, 270)
        self.hideturtle()
        self.write(arg=f"score {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def tablo(self):
        self.clear()
        self.score += 1
        self.write(arg=f"score {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0 ,0)
        self.write(arg=f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)
