from turtle import Screen, Turtle
from player import Player

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

player1 = Player()



screen.exitonclick()