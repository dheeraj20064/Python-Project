# import colorgram
# coloring=[]
# colors=colorgram.extract('dot.jpg',30)
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     coloring.append((r,g,b))
# print(coloring)
import turtle as t
import random
tim=t.Turtle()
tim.speed("fastest")
tim.hideturtle()
tim.penup()

colours=[ (239, 242, 247), (198, 165, 116), (144, 79, 55), (221, 201, 138), (58, 93, 121), (167, 153, 48), (132, 34, 23), (137, 162, 181), (69, 40, 34), (51, 117, 87), (195, 93, 75), (146, 178, 150), (18, 93, 72), (231, 176, 165), (162, 143, 158), (35, 60, 75), (105, 73, 77), (180, 204, 177), (148, 19, 23), (83, 147, 127), (70, 37, 40), (18, 70, 60), (27, 82, 88), (40, 66, 89), (190, 86, 89), (68, 64, 58), (223, 176, 180)]

t.colormode(255)
total_dots=100
tim.setheading(225)
tim.forward(300)


for i in range(1,total_dots+1):
    tim.setheading(0)
    tim.dot(20,random.choice(colours))
    tim.forward(50)

    if i%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
screen=t.Screen()
screen.exitonclick()


