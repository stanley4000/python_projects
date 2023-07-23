from turtle import Turtle, Screen


screen = Screen()

tim = Turtle()
def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.bk(10)


def turn_right():
    tim.rt(10)


def turn_left():
    tim.lt(10)


def clear():
    tim.penup()
    tim.home()
    tim.clear()
    tim.pendown()



screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='c', fun=clear)
screen.exitonclick()
