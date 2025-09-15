from turtle import Turtle, Screen
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)
        self.setheading(90)




    def up(self):
        new_y=self.ycor()+20
        self.goto(self.xcor(), new_y)
    def down(self):
        new_y=self.ycor()-20
        self.goto(self.xcor(), new_y)


