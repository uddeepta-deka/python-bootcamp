# import colorgram
#
# # Extract colors from 'img.jpg'
# rgb_colors = []
# colors = colorgram.extract('img.jpg', 30)
# for color in colors:
#     rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
#
# print(rgb_colors)

from turtle import Turtle, Screen, colormode
from random import choice

color_list = [(139, 164, 184), (27, 114, 171), (202, 141, 167), (237, 213, 67), (219, 157, 89), (22, 136, 66), (139, 21, 37), (124, 72, 94), (185, 176, 26), (70, 30, 37), (182, 73, 41), (225, 170, 197), (52, 36, 34), (232, 83, 40), (39, 174, 99), (108, 190, 136), (9, 107, 64), (29, 169, 185), (181, 95, 112), (38, 37, 43), (239, 216, 8), (188, 184, 210), (158, 207, 215), (152, 214, 174), (240, 169, 154), (105, 41, 39)]
tim = Turtle()
screen = Screen()
colormode(255)


def draw_dots(turtle_name, number_of_dots=10, spacing=50, dot_size=20):
    turtle_name.speed("fastest")
    turtle_name.hideturtle()
    turtle_y = -200
    for _ in range(number_of_dots):
        turtle_x = -225
        for _ in range(number_of_dots):
            turtle_name.penup()
            turtle_name.setpos(turtle_x, turtle_y)
            turtle_name.pendown()
            turtle_name.dot(dot_size, choice(color_list))
            turtle_x += spacing
        turtle_y += spacing


draw_dots(tim)
screen.exitonclick()