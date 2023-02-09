from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


def read_data():
    with open("..\..\data.txt", mode="r") as data:
        contents = data.read()
    return contents


def data_write(score):
    with open("..\..\data.txt", mode="w") as data:
        contents = data.write(f"{score}")
    return contents


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(read_data())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def rest(self):
        if self.score > self.high_score:
            self.high_score = self.score
            data_write(self.high_score)
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
