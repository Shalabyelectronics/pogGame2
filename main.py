from turtle import Screen
from paddle import Paddle
from ball import Ball
import random
import time

# RIGHT_PADDLE = [135, 180, 225]
# LEFT_PADDLE = [45, 0, 315]

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
screen.update()
screen.listen()
screen.onkeypress(key="w", fun=right_paddle.move_up)
screen.onkeypress(key="s", fun=right_paddle.move_down)
screen.onkeypress(key="Up", fun=left_paddle.move_up)
screen.onkeypress(key="Down", fun=left_paddle.move_down)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.rest_position()




screen.exitonclick()
