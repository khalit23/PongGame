from turtle import Turtle

MOVE_DISTANCE = 30


class Player(Turtle):

    def __init__(self, position):
        super(Player, self).__init__()
        self.shape("square")
        self.shapesize(stretch_wid=6, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)