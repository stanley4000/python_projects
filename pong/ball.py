from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color("yellow")
        self.speed("fastest")
        self.goto(0, 0)

    def move(self, speed):
        self.forward(speed)
