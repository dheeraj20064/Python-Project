import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S.States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

GUESS=0
states=[]

data=pandas.read_csv("50_states.csv")
data_state=data.state.to_list()

while GUESS<50:
    answer_text = screen.textinput(title=f"{GUESS}/50 States Correct ", prompt="What's another state name?").title()
    if answer_text == "Exit":
        missing_states=[n for n in data_state if n not in states ]
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("Remaining_states.csv")
    if answer_text in data_state and answer_text not in states:
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_text]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_text)
        states.append(answer_text)
        GUESS=GUESS+1