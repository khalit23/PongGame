from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed = 0.05
        self.y_readjust = 10
        self.x_readjust = 10

    def start(self):
        new_x = self.xcor() + self.x_readjust
        new_y = self.ycor() + self.y_readjust
        self.goto(new_x, new_y)

    def change_direction_y(self):
        self.y_readjust *= -1

    def change_direction_x(self):
        self.x_readjust *= -1
        self.speed *= 0.85

    def reset(self):
        self.goto(0, 0)
        self.speed = 0.05

