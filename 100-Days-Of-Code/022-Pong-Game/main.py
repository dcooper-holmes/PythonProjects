import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
screen.title("Pong")

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
scoreboard = Scoreboard()
ball = Ball()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.move_speed *= 0.9

    #Detect if right paddle misses ball
    if ball.xcor() > 380 :
        ball.reset_position()
        scoreboard.l_point()
        ball.move_speed = 0.1

    # Detect if right paddle misses ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        ball.move_speed = 0.1

screen.exitonclick()