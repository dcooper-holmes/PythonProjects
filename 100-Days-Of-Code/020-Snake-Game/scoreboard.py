from turtle import Turtle

class ScoreBoard(Turtle):

    score = 0
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.ht()
        self.goto(0, 280)
        self.write(f"Score = {self.score}", False, align="center")

    def UpdateScore(self):
        self.clear()
        self.score += 1
        self.write(f"Score = {self.score}", False, align="center")