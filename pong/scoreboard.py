from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, score, position):
    #position argument (x, y)
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("blue")
        self.goto(position)
        self.get_score(score)


    def get_score(self, score):
        self.clear()
        self.write(arg=score, move=False, align='center', font=('Arial', 18, 'normal'))