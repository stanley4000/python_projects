from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_POSITIONS = [-230, -190, -150, -110, -70, -30, 10, 50, 90, 130, 170, 210, 250]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.car_speed = STARTING_MOVE_DISTANCE
        self.cars = []

    def create_car(self):
        random_chance = random.randint(1, 6)
        # This loop controls rate of car creation
        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            position = random.choice(STARTING_POSITIONS)
            new_car.goto(300, position)
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def reset_speed(self):
        self.car_speed += MOVE_INCREMENT
