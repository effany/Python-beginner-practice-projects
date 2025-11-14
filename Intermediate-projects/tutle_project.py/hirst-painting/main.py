import colorgram as cg
from turtle import Turtle, Screen
import turtle as t
import random

t.colormode(255)  # Set color mode to use RGB values 0-255
tom = Turtle()
tom.penup()
tom.hideturtle()
tom.speed("fastest")

# Move to left middle of canvas
tom.goto(-200, -200)

color_list = [(110, 95, 72), (175, 160, 135), (50, 40, 27), (227, 217, 193), (211, 199, 158), (33, 38, 43), (148, 133, 96), (31, 36, 34), (80, 68, 38), (227, 216, 224), (170, 157, 163), (38, 32, 35), (216, 216, 224), (98, 89, 93), (84, 89, 96), (89, 96, 92), (158, 159, 170), (146, 160, 152), (217, 227, 221), (79, 59, 50), (144, 122, 113), (201, 185, 194), (209, 185, 177), (185, 185, 209), (137, 121, 129), (69, 60, 64), (59, 62, 72), (92, 149, 123), (122, 123, 140), (59, 66, 62)]

def draw_dot_line(dots):
    for _ in range(dots):
        color = random.choice(color_list)
        tom.dot(20, color)
        tom.penup()
        tom.forward(20)
        tom.penup()
        tom.forward(20)

def draw_dot_canva(lines, dots):
    for _ in range(lines):
        print(tom.position())
        draw_dot_line(dots)
        tom.penup()
        y_position = tom.position()[1] + 50
        tom.goto(-200, y_position)  # Return to left side for next row

draw_dot_canva(10, 10)

my_screen = Screen()
my_screen.exitonclick()



# colors = cg.extract("color.jpg", 30)
# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)
