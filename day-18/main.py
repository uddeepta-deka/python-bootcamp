from turtle import Turtle, Screen, colormode
from random import randint, choice

tim = Turtle()
screen = Screen()


def draw_a_square(turtle_name):
    for _ in range(4):
        turtle_name.forward(100)
        turtle_name.left(90)


def draw_dashed_lines(turtle_name, steps=10):
    for _ in range(steps):
        turtle_name.pendown()
        turtle_name.forward(10)
        turtle_name.penup()
        turtle_name.forward(10)


def draw_polygons(turtle_name, n):
    for sides in range(3, n+1):
        exterior_angle = 360 / sides
        turtle_name.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
        for _ in range(sides):
            turtle_name.forward(75)
            turtle_name.right(exterior_angle)


def random_walk(turtle_name, steps=20):
    direction = ["left", "right"]
    turtle_name.speed("fastest")
    for _ in range(steps):
        turtle_name.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
        turtle_name.pensize(randint(1, 10))
        turtle_name.forward(randint(5, 40))
        d = choice([0, 90, 180, 270])
        turtle_name.setheading(d)


def draw_spirograph(turtle_name, num_circles=10):
    angle = 360/num_circles
    turtle_name.speed("fast")
    for _ in range(num_circles):
        turtle_name.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
        turtle_name.circle(80)
        turtle_name.setheading(turtle_name.heading()+angle)


tim.shape("turtle")
colormode(255)
# draw_a_square(tim)
# draw_dashed_lines(tim)
# draw_polygons(tim, 10)
# random_walk(tim, 200)
draw_spirograph(tim, 15)

screen.exitonclick()
