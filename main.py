from turtle import Screen
from ball import Ball
from player import Player
from score import Score
import time

FONT = ("Courier", 40, "normal")
ALIGN = "center"

screen = Screen()
screen.setup(width=1000, height=700)
screen.bgcolor("black")
screen.tracer(0)
screen.title(f"Khalit's Pong Game!")

ball = Ball()
player_1 = Player((-450, 0))
player_2 = Player((450, 0))
score_1 = Score((-250, 275))
score_2 = Score((250, 275))

screen.listen()
screen.onkey(fun=player_2.move_up, key="Up")
screen.onkey(fun=player_2.move_down, key="Down")
screen.onkey(fun=player_1.move_up, key="w")
screen.onkey(fun=player_1.move_down, key="s")

start_game = True

while start_game:
    screen.update()
    time.sleep(ball.speed)

    ball.start()

    if ball.ycor() > 330 or ball.ycor() < -330:
        ball.change_direction_y()

    if ball.xcor() > 420 and ball.distance(player_2) < 50:
        ball.change_direction_x()

    if ball.xcor() < -420 and ball.distance(player_1) < 50:
        ball.change_direction_x()

    if ball.xcor() > 450:
        score_1.increase_score()
        ball.reset()

    if ball.xcor() < -450:
        score_2.increase_score()
        ball.reset()

    if score_1.score == 5:
        start_game = False
        ball.write("Player 1 wins!", font=FONT, align=ALIGN)

    if score_2.score == 5:
        start_game = False
        ball.write("Player 2 wins!", font=FONT, align=ALIGN)

screen.exitonclick()