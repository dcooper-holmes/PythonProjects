from turtle import Turtle

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        
        score = 0
        self.write(f"Score = {score}", True, align="center")

    def UpdateScore(self):
        score += 1
        self.write(f"Score = {score}", True, align="center")