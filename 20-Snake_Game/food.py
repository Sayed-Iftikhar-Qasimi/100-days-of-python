from turtle import Turtle
import random
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("purple")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(self.coordinates())

    def coordinates(self):
        x_coordinate = random.randint(-280,280)
        y_coordinate = random.randint(-280,280)
        return (x_coordinate,y_coordinate)
