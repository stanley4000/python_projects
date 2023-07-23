import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # create and move cars
    car.create_car()
    car.move()
    # Detect up arrow control
    screen.listen()
    screen.onkey(player.move, "Up")
    # Detect collisions with cars, end game
    for x in car.cars:
        # if x.xcor() - player.xcor() <= 30 and x.ycor() - player.ycor() <= 20:
        #     print("ouch")
        if player.distance(x.position()) <= 20:
            print("ouch")
            player.shape("square")
            scoreboard.game_over()
            game_is_on = False
    # Detect crossing finish line, reset turtle and change car speed
    if player.ycor() >= 290:
        scoreboard.score += 1
        scoreboard.get_score(scoreboard.score)
        player.sety(-280)
        car.reset_speed()

screen.exitonclick()
