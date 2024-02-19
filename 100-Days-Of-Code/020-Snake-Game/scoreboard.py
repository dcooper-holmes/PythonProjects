from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class ScoreBoard(Turtle):

    score = 0
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.ht()
        self.goto(0, 260)
        self.Update_ScoreBoard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        

    def Update_ScoreBoard(self):
        self.write(f"Score = {self.score}", False, align=ALIGNMENT, font=FONT)

    def UpdateScore(self):
        self.score += 1
        self.clear()
        self.Update_ScoreBoard()