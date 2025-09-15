from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score

import time

 

screen = Screen()
food = Food()
score=Score()
snake = Snake()

screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0)



screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



game_notover=True
while game_notover:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_notover=False
        score.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_notover=False
            score.game_over()




screen.exitonclick()