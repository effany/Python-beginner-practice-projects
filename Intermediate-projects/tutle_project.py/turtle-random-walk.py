from turtle import Turtle, Screen
import turtle as t
import random

tom = Turtle()
tom.shape("turtle")
tom.pensize(15) 
tom.speed("fastest")
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

angle_array = [0, 90, 180, 270]

def random_walk(steps):
    for _ in range(steps):
        tom.forward(30)
        tom.setheading(random.choice(angle_array))
        color = random_color()
        tom.pencolor(color)

random_walk(200)


my_screen = Screen()
my_screen.exitonclick()
