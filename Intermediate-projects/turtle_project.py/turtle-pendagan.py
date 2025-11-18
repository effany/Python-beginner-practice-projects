from turtle import Turtle, Screen
import turtle as t
import random

tom = Turtle()
tom.shape("turtle")


range_count = 3
right_angle = 120

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tom.forward(100)
        tom.right(angle)

for shape_side_n in range(3, 11):
    draw_shape(shape_side_n)

my_screen = Screen()
my_screen.exitonclick()
