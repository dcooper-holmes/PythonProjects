from turtle import Turtle

SCORE = 0

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        
        score = SCORE
        
        self.color("white")
        self.penup()
        self.ht()

        self.write(f"Score = {score}", True, align="center")