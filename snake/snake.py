
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
from turtle import Turtle
class Snake:


    def __init__(self):
        self.turtle_list = []
        self.create_snake()
        self.head = self.turtle_list[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
        turtle = Turtle(shape="square")
        self.turtle_list.append(turtle)
        turtle.penup()
        turtle.color("white")
        turtle.goto(position)

    def extend(self):
        #Add a new segment to the snake
        self.add_segment(self.turtle_list[-1].position())

    def move(self):
        for segment in range(len(self.turtle_list) - 1, 0, -1):
        # this controls movement of segments from last to first
            new_x = self.turtle_list[segment - 1].xcor()
            new_y = self.turtle_list[segment - 1].ycor()
            self.turtle_list[segment].goto(new_x, new_y)
        # This moves the first segment
        self.head.forward(MOVE_DISTANCE)

    def reset_snake(self):
        for segment in self.turtle_list:
            segment.goto(1000, 1000)
        self.turtle_list = []
        self.create_snake()
        self.head = self.turtle_list[0]



    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)