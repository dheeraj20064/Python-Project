from turtle import Turtle
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP=90
DOWN=270
LEFT=180
RIGHT=0




class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.snake_body(position)

    def snake_body(self,position):
        new_position = Turtle("square")
        new_position.color("white")
        new_position.penup()
        new_position.goto(position)
        self.segments.append(new_position)

    def extend(self):
        self.snake_body(self.segments[-1].position())
    def move_snake(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            x =self.segments[segment - 1].xcor()
            y =self.segments[segment - 1].ycor()
            self.segments[segment].goto(x, y)
        self.segments[0].forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

