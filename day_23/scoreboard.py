from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.shape()
        self.penup()
        self.pencolor("black")
        self.speed(100)
        self.goto(-220, 260)
        self.hideturtle()
        self.write(arg=f"Level: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def tablo(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Level: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)
