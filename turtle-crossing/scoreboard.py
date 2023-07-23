from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(130, 260)
        self.color("black")
        self.score = 1
        self.get_score(self.score)

    def get_score(self, score):
        self.clear()
        self.write(arg=f"Level: {score}", move=False, align='left', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align='center', font=FONT)
