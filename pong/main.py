from ball import Ball
from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
import random
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG!")
screen.tracer(0)


paddle = Paddle((350, 0))
cpu_paddle = Paddle((-350, 0))
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
ball = Ball()
SPEED = 20
score = 0
cpu_score = 0
scoreboard = Scoreboard(score=score, position=(300, 250))
scoreboard_cpu = Scoreboard(score=cpu_score, position=(-300, 250))


# def check_rect_collision(a, b):
#     # returns TRUE if ball(a) detected to be within outline of paddle(b)
#     return abs(a.xcor() - b.xcor()) < PADDLE_WIDTH/2 and abs(a.ycor() - b.ycor()) < PADDLE_HEIGHT/2
game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move(SPEED)
    # Detect up and down arrow controls
    screen.listen()
    screen.onkey(paddle.up, "Up")
    screen.onkey(paddle.down, "Down")

    # detect collision with paddles
    if ball.distance(paddle) < 50 and ball.xcor() >= 339 or ball.distance(cpu_paddle) < 50 and ball.xcor() <= -339:
        # change direction and increase speed
        SPEED *= -1.1
        #add random angle to ball
        angle = random.randint(-3, 3)
        new_heading = -1 * (ball.heading() + angle * 10)
        ball.setheading(new_heading)


    # # detect collision with back walls, increase score and reset ball position, direction and speed
    if ball.xcor() > 390:
        cpu_score += 1
        scoreboard_cpu.get_score(cpu_score)
        ball.goto(0, 0)
        ball.setheading(0)
        SPEED = -20
    if ball.xcor() < -390:
        score += 1
        scoreboard.get_score(score)
        ball.goto(0, 0)
        ball.setheading(0)
        SPEED = 20

    # detect collision with side walls and change angle

    if ball.ycor() > 290 or ball.ycor() < -290:
        new_heading = -1 * ball.heading()
        ball.setheading(new_heading)

    #control cpu paddle
    if cpu_paddle.ycor() < ball.ycor():
        cpu_paddle.up()
    if cpu_paddle.ycor() > ball.ycor():
        cpu_paddle.down()

screen.exitonclick()
