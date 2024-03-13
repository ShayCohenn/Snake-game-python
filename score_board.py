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
        with open('data.txt', 'r') as f:
            self.high_score = int(f.read())
        self.update_text()

    def update_text(self):
        """Write the score text, 1.clear, 2.go to the position, 3.write"""
        self.clear()
        self.goto(0,250)
        self.write(f"Score = {self.score} High Score = {self.high_score}", align="center",move=True,font=FONT)

    def increase_score(self):
        """Increment the score by 1 and call the update text method"""
        self.score += 1
        self.update_text()

    def reset_scoreboard(self):
        """Reset the scoreboard and save high score to data.txt"""
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', 'w') as f:
                f.write(str(self.high_score))
        self.score = 0
        self.update_text()