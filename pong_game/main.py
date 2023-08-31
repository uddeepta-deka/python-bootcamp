from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

STARTING_POSITION_RIGHT = (350, 0)
STARTING_POSITION_LEFT = (-350, 0)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(STARTING_POSITION_RIGHT)
l_paddle = Paddle(STARTING_POSITION_LEFT)

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320\
            or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect when r_paddle misses the ball
    if ball.xcor() > 380:
        time.sleep(0.5)
        ball.reset_position()
        scoreboard.l_point()

    # detect when l_paddle misses the ball
    if ball.xcor() < -380:
        time.sleep(0.5)
        ball.reset_position()
        scoreboard.r_point()

    if scoreboard.l_score == scoreboard.max_score or scoreboard.r_score == scoreboard.max_score:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()