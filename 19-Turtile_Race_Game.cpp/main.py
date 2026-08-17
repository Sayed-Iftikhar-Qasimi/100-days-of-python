from turtle import Turtle, Screen
import random

def move_forward():
    movement = random.randint(0,10)
    return movement


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)

is_race_on = False

turtle_colors = ["red","blue","yellow","green", "purple","orange"]
y_coordinates = [-50,-10,30,60,90,120]

user_bet = screen.textinput(
    title = "****Turtle Race****",
    prompt = "Which turtle will win the race? Enter a color: ").lower()

all_turtles = []

if user_bet in turtle_colors:

    for i in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(turtle_colors[i])
        new_turtle.goto(x=-380, y=y_coordinates[i])
        all_turtles.append(new_turtle)

    is_race_on = True
    while is_race_on:

        for turtle in all_turtles:
            turtle.forward(move_forward())
            if turtle.xcor() > 380:
                is_race_on = False
                winner_color = turtle.pencolor()
                if winner_color == user_bet:
                    print(f"You've won! The {winner_color} turtle is the winner! ")
                else:
                    print(f"You've lost! The {winner_color} turtle is the winner!")
                break
    screen.exitonclick()


else:
    print("Invalid Color!")
    screen.bye()








