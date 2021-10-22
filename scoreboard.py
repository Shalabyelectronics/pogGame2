from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.r_score = 0
        self.l_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def update_r_score(self):
        self.r_score += 1
        self.update_score()

    def update_l_score(self):
        self.l_score += 1
        self.update_score()

    def check_winner(self):
        if self.r_score == 5:
            self.home()
            self.write("Right player Won", align="center", font=("Courier", 40, "normal"))
            return True
        if self.l_score == 5:
            self.home()
            self.write("Left player Won", align="center", font=("Courier", 40, "normal"))
            return True
