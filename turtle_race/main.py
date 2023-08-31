from turtle import Turtle, Screen, colormode
import random

screen = Screen()
width = 500
height = 400
screen.setup(width=width, height=height)
is_race_on = False

user_bet = screen.textinput(title="Make your bet: ", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "blue", "green", "purple"]
all_turtles = list()
dy = 40
y_pos = -120
for color in colors:
    y_pos += dy
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-width / 2 + 20, y=y_pos)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        turtle.forward(random.randint(0, 10))


screen.exitonclick()