from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("oh, wow a snake.")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    # The following functions control speed and refresh rate of animation
    screen.update()
    time.sleep(.1)
    snake.move()
    # Display scoreboard

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        print("OH SHIT")
        # Update score
        scoreboard.increase_score()
        # extend snake
        snake.extend()
    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        # game_is_on = False
        scoreboard.reset_game()
        snake.reset_snake()
        # scoreboard.game_over()
    # Detect collision with tail
    for segment in snake.turtle_list[1:]:
        if snake.head.distance(segment) < 7:
            print("ouch!")
            # game_is_on = False
            scoreboard.reset_game()
            snake.reset_snake()
            # scoreboard.game_over()

screen.exitonclick()
