from turtle import Turtle
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

tim = Turtle()

counter = 0
counter_side = 3

while counter < 8:
    turning_angle = 360 / counter_side

    tim.color(colors[counter])

    for side in range(counter_side):
        tim.forward(100)
        tim.right(turning_angle)

    counter += 1
    counter_side += 1
