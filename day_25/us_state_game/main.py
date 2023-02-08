import turtle
from turtle import Screen, Turtle
import pandas

FONT = ("Courier", 12, "normal")
ALIGNMENT = "center"

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{len(data)} State Correct",
                                    prompt="Whats another state's name?")
    answer_state_lower = answer_state.title()
    if answer_state_lower == "Exit":
        break
    for state in data.state:
        if answer_state_lower == state:
            guessed_states.append(answer_state_lower)
            state_turtl = Turtle()
            coor = data[data.state == state]
            coor_dict = coor.to_dict()
            for i in coor_dict:
                if i == "x":
                    for key in coor_dict[i]:
                        new_coor_x = coor_dict[i][key]
                        print(new_coor_x)
                elif i == "y":
                    for key in coor_dict[i]:
                        new_coor_y = coor_dict[i][key]
                        print(new_coor_y)
            state_turtl.hideturtle()
            state_turtl.penup()
            state_turtl.goto(new_coor_x, new_coor_y)
            state_turtl.write(arg=state, move=False, align=ALIGNMENT, font=FONT)

for item in guessed_states:
    if item in all_states:
        all_states.remove(item)

new_csv = pandas.DataFrame(all_states)

new_csv.to_csv("states_to_learn.csv")

