from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput("Make your bet!", "Which turtle will win the race? Enter a color: ")
print(user_bet)


screen.exitonclick()