import turtle
from turtle import Screen, Turtle
import pandas

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
data_l = data["state"]

coor = data[data.state == "Texas"]
coor_l = coor.to_dict()
print(coor_l)
score = 0

go_next = True
while go_next:
    answer_state = screen.textinput(title=f"{score}/{len(data)} State Correct",
                                    prompt="Whats another state's name?")
    answer_state_lower = answer_state.title()
    print(answer_state_lower)
    for state in data.state:
        if answer_state_lower == state:
            score += 1
            state_turtl = Turtle()
            coor = data[data.state == state]
            coor_dict = coor.to_dict()
            state_turtl.goto(coor_dict["x"][42], coor_dict["y"][42])
            state_turtl.write(arg=state, move=False, align=ALIGNMENT, font=FONT)
            print("TRRR")
