import colorgram as cg
from turtle import Turtle, Screen
import turtle as t
import random

t.colormode(255)  # Set color mode to use RGB values 0-255
tom = Turtle()
tom.penup()
tom.hideturtle()
tom.hideturtle()
tom.speed("fastest")

color_list = [(110, 95, 72), (175, 160, 135), (50, 40, 27), (227, 217, 193), (211, 199, 158), (33, 38, 43), (148, 133, 96), (31, 36, 34), (80, 68, 38), (227, 216, 224), (170, 157, 163), (38, 32, 35), (216, 216, 224), (98, 89, 93), (84, 89, 96), (89, 96, 92), (158, 159, 170), (146, 160, 152), (217, 227, 221), (79, 59, 50), (144, 122, 113), (201, 185, 194), (209, 185, 177), (185, 185, 209), (137, 121, 129), (69, 60, 64), (59, 62, 72), (92, 149, 123), (122, 123, 140), (59, 66, 62)]

tom.setheading(225)
tom.forward(300)
tom.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tom.dot(20, random.choice(color_list))
    tom.forward(50)

    if dot_count % 10 == 0:
        tom.setheading(90)
        tom.forward(50)
        tom.setheading(180)
        tom.forward(500)
        tom.setheading(0)

my_screen = Screen()
my_screen.exitonclick()