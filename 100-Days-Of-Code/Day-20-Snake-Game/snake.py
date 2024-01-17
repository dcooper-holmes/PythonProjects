from turtle import Turtle
import time

class Snake:

    def __init__(self):
        starting_positions = [(0, 0), (-20, 0), (-40, 0)]

        segments = []

        for position in starting_positions:

            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)

            segments.append(new_segment)

    def move(self):        
                
        for segment_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_num - 1].xcor()
            new_y = self.segments[segment_num - 1].ycor()
            self.segments[segment_num].goto(new_x, new_y)