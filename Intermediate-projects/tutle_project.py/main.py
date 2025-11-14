from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("chocolate")

for _ in range(4):
    timmy.right(90)
    timmy.forward(100)


timmy.left(90)
timmy.forward(100)

for _ in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

my_screen = Screen()
my_screen.exitonclick()


