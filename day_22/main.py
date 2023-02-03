from day_22.ball import Ball
from turtle import Turtle, Screen
from day_22.paddle import Paddle
import time
from day_22.scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()
screen.onkey(key="w", fun=paddle_l.go_up)
screen.onkey(key="s", fun=paddle_l.go_down)
screen.onkey(key="Up", fun=paddle_r.go_up)
screen.onkey(key="Down", fun=paddle_r.go_down)

bol_go = True
while bol_go:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_bol_start()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detected paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_point()

    # Detect R paddle misses
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.r_point()


screen.exitonclick()
