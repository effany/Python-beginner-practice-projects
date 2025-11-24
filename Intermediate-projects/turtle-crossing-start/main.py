import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()

new_cars = []

game_is_on = True

screen.listen()
screen.onkey(key="Up", fun=player.move_up)
screen.onkey(key="Left", fun=player.move_left)
screen.onkey(key="Right", fun=player.move_right)

def add_new_car():
    y_pos = random.randint(-220,230)
    car = CarManager(x_pos = 300, y_pos = y_pos)
    new_cars.append(car)

while game_is_on:
    time.sleep(0.1)
    screen.update()

    if len(new_cars) ==0:
        add_new_car()
    elif new_cars[-1].xcor() < 250:
        add_new_car()

    for car in new_cars:
        car.move()
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
        elif player.ycor() >= 230:
            scoreboard.level_up()
            player.reset_position()
            for car in new_cars:
                car.hideturtle()
            new_cars.clear()
            CarManager.level_up()

              
screen.exitonclick()
