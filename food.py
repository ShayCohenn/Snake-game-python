import random
from turtle import Turtle

class Food(Turtle):

    def __init__(self):
        """Initialize the food class using the Turtle class"""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Set the food's position to a random (x,y) coordinates"""
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x, random_y)