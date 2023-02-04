from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = -10
place_x = 300


class CarManager:

    def __init__(self):
        self.ga_cars = []
        # self.create_car()

    def create_car(self):
        cars = Turtle("square")
        cars.shape("square")
        cars.color(random.choice(COLORS))
        cars.shapesize(stretch_wid=1, stretch_len=2)
        cars.penup()
        y = random.randint(-250, 250)
        cars.goto(place_x, y)
        self.ga_cars.append(cars)

    def move(self):
        for car in self.ga_cars:
            car.forward(MOVE_INCREMENT)

