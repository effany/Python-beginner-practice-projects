from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def counter_clockwise():
    tim.circle(100, 10)

def clockwise():
    tim.circle(-100, 10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def set_keys(key, fun):
    screen.listen()
    screen.onkey(key=key, fun=fun)


set_keys("w", move_forwards)
set_keys("s", move_backwards)
set_keys("a", turn_left)
set_keys("d", turn_right)
set_keys("c", clear_screen)

screen.exitonclick()