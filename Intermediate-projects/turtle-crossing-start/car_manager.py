from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3


class CarManager(Turtle):
    
    current_speed = STARTING_MOVE_DISTANCE
    
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.shapesize(1,2)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(x_pos, y_pos)
       

    def move(self):
        self.backward(CarManager.current_speed)

    @classmethod
    def level_up(cls):
        cls.current_speed += MOVE_INCREMENT

        
