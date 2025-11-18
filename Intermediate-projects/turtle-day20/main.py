from turtle import Turtle, Screen 
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which tutrle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
all_turtles = []

y_start = -100
is_race_on = False

for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    y_start += 30
    new_turtle.goto(x=-230, y=y_start)
    all_turtles.append(new_turtle)

if user_bet: 
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230.0:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The winner is {winning_color}")
            else:
                print(f"You've LOST!! The winner is {winning_color}")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()