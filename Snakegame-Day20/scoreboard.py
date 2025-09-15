from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.total_score = 0
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.write(f"Score {self.total_score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def increase_score(self):
        self.total_score += 1
        self.clear()
        self.goto(0, 260)
        self.write(f"Score {self.total_score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):

        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)



