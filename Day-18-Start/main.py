from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")
# for i in range(4):
#     timmy.forward(100)
#     timmy.left(90)
# import heroes
#
# print(heroes.gen())
for _ in range(40):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()
