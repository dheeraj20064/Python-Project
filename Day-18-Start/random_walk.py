import turtle as t
import random
tim=t.Turtle()
tim.speed("fastest")

list=[0,90,180,270]


def random_walk(num):
    for i in range(num+1):
        tim.setheading(random.choice(list))
        tim.forward(10)
random_walk(100)
