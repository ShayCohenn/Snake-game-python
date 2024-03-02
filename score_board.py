from turtle import Turtle

FONT = ("Courier", 15, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        """Initializing the score board class using the turtle class."""
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_text()

    def update_text(self):
        """Write the score text, 1.clear, 2.go to the position, 3.write"""
        self.clear()
        self.goto(0,250)
        self.write(f"Score = {self.score} ", align="center",move=True,font=FONT)

    def increase_score(self):
        """Increment the score by 1 and call the update text method"""
        self.score += 1
        self.update_text()

    def game_over(self):
        """Write game over text"""
        self.goto(0,0)
        self.write("Game Over, Press 'R' to restart", align="center",move=True,font=FONT)