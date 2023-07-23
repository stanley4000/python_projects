from turtle import Turtle



class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(110, 240)
        self.color("white")
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.get_score()


    def get_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}\nHigh Score: {self.high_score}", move=False, align='left', font=('Arial', 18, 'normal'))


    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            new_high_score = str(self.score)
            with open("data.txt", mode="w") as file:
                file.write(new_high_score)
        self.score = 0
        self.get_score()


    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align='center', font=('Arial', 18, 'normal'))

    def increase_score(self):
        self.score +=1
        self.get_score()