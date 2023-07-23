from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []
y_index = [170, 100, 30, -40, -110, -180]
for turtles in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    turtle_list.append(new_turtle)
    new_turtle.penup()
    new_turtle.color(f"{colors[turtles]}")
    new_turtle.goto(x=-230, y=y_index[turtles])
race_on = False
if user_bet:
    race_on = True
while race_on:
    for turtles in turtle_list:
        speed = random.randint(0, 10)
        turtles.forward(speed)
        if turtles.xcor() >= 230:
            winning_color = turtles.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle won!")
            else:
                print(f"You lost! The {winning_color} turtle won!")
            race_on = False







screen.exitonclick()
