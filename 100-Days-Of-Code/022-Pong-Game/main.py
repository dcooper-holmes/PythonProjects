from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
screen.title("Pong")

screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")

game_is_on = True

while game_is_on:
    screen.update()

screen.exitonclick()