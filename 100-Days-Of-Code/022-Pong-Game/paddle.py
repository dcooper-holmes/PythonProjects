from turtle import Turtle

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        Paddle.shape("square")
        Paddle.color("white")
        Paddle.shapesize(stretch_wid=5, stretch_len=1)
        Paddle.penup()
        Paddle.goto(350, 0)