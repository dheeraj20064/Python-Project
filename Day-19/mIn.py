import turtle as t
tim=t.Turtle()
tim.shape("turtle")
screen=t.Screen()

def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def move_left():
    new_heading=tim.heading() + 10
    tim.setheading(new_heading)
def move_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.home()
    tim.clear()
    



screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_backward,"s")
screen.onkey(move_left,"a")
screen.onkey(move_right,"d")
screen.onkey(clear,"c")



screen.exitonclick()