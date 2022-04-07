from turtle import Turtle

FONT = ("Courier", 60, "normal")


class Score(Turtle):

    def __init__(self, position):
        super(Score, self).__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.write(self.score, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(self.score, font=FONT)


