from turtle import Turtle, Screen
import turtle as t
import random

tom = Turtle()
tom.shape("turtle")
tom.speed("fastest")
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

def draw(rad):
    for i in range(2):
        tom.circle(rad, 90)
        tom.circle(rad//2, 90)

def draw_spirograph(size_of_gape):
    for _ in range(int(360 / size_of_gape)):
        color = random_color()
        tom.pencolor(color)
        current_heading = tom.heading()
        tom.setheading(current_heading + size_of_gape)
        draw(100)

draw_spirograph(5)

my_screen = Screen()
my_screen.exitonclick()