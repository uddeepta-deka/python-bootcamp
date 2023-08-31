from turtle import Turtle

FONT = ("Courier", 60, "normal")
ALIGNMENT = "center"
MAX_SCORE = 5


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.max_score = MAX_SCORE
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        if self.l_score == self.max_score:
            self.goto(0, 0)
            self.write("PLAYER 'L' WINS!", align=ALIGNMENT, font=FONT)
        elif self.r_score == self.max_score:
            self.goto(0, 0)
            self.write("PLAYER 'R' WINS!", align=ALIGNMENT, font=FONT)