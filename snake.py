from turtle import Turtle

STARTING_POSITIONS = [(0,0,), (-20,0), (-40,0)]
MOVE_DISTANCE = 5

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Create the first 3 segments of the snake"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Create a segment method and append it to the segments list"""
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset_snake(self):
        """Reset the snake when game is resetting"""
        for seg in self.segments:
            seg.reset()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend_snake(self):
        """Extend the snake mid game"""
        self.add_segment(self.segments[-1].position())
        
    def move(self):
        """Starting from the end of the segments list each segment will go to the position of the next one,
        the head segment goes forward"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_X_cor = self.segments[seg_num - 1].xcor()
            new_y_cor = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_X_cor, new_y_cor)
        self.segments[0].forward(MOVE_DISTANCE)

    def turn_north(self):
        """If the snake isn't facing south then turn north because the snake can't do a 180deg turn"""
        if self.head.heading() != 270:
            self.head.seth(90)

    def turn_south(self):
        """If the snake isn't facing north then turn south"""
        if self.head.heading() != 90:
            self.head.seth(270)

    def turn_east(self):
        """If the snake isn't facing west then turn east"""
        if self.head.heading() != 180:
            self.head.seth(0)

    def turn_west(self):
        """If the snake isn't facing east then turn west"""
        if self.head.heading() != 0:
            self.head.seth(180)
    