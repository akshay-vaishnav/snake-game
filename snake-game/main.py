# here we are creating program for snake game
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import random
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0) #Turn snake animation on/off and set delay for update drawings so when snake is run we dont see any break.

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update() #so after screen.tracer(0) we need to show the updated position of snake so we use screen.update()
    time.sleep(0.2) #time module is use to slow down the screen time, its show 0.2 second delay after the screen update so we can see the moving snake easily

    snake.move()

    if snake.head.distance(food) < 15: #here we are detecting collision of snake with food so we know that food is 10x10 so when the snake comes near the food hence less than 15.
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # game_is_on = False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()

    #detect collision with tail
    for segment in snake.segments[1:]: #here we are using python slicing function in which include all in segment except head segment
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()















screen.exitonclick()

























