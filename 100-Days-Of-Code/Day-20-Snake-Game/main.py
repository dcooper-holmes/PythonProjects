from turtle import Screen, Turtle
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()

    screen.onkey(fun=snake.up, key="Up")
    screen.onkey(fun=snake.down, key="Down")
    screen.onkey(fun=snake.left, key="Left")
    screen.onkey(fun=snake.right, key="Right")

    screen.listen()


screen.exitonclick()