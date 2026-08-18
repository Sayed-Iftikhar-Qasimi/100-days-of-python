from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

def change_direction():
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

change_direction()
screen.listen()

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

#   Detect Collision with food
    if snake.head.distance(food) <= 12:
        food.refresh()
        scoreboard.increase_score()
        snake.extend_snake()

#   Detect Collision with wall
    if snake.head.xcor() < -280 or snake.head.xcor() > 280  or snake.head.ycor() > 280 or snake.head.ycor() < -280:
           scoreboard.game_over()
           is_game_on = False

#   Detect tail collision
    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()
            print("Tails Collision happened.")






screen.exitonclick()