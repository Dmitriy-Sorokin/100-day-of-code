import time
from turtle import Screen
from day_23.player import Player
from day_23.car_manager import CarManager
from day_23.scoreboard import Scoreboard
counter = 0

screen = Screen()
cars = CarManager()
player = Player()
tablo = Scoreboard()
player.start_p()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)
screen.listen()
screen.onkey(key="w", fun=player.go_up)
screen.onkey(key="s", fun=player.go_down)

game_is_on = True
while game_is_on:
    counter += 1
    time.sleep(player.move_speed)
    screen.update()
    if counter % 6 == 0:
        cars.create_car()
    cars.move()

    # Crossing successfully
    if player.ycor() > 280:
        player.start_p()
        player.m_speed()
        tablo.tablo()

    # Detected car
    for car in cars.ga_cars:
        if player.distance(car) < 25:
            tablo.game_over()
            game_is_on = False


screen.exitonclick()
