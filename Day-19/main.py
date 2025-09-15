from turtle import Turtle,Screen

screen = Screen()


screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet", prompt="What colour do you choose")
colors = ["red","blue","green","yellow","cyan","magenta"]
x=-230
y=-100
for _ in range(6):
    tim=Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[_])
    tim.goto(x,y)
    y=y+40





screen.exitonclick()