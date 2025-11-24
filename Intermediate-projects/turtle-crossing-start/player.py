from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.x_pos = 0
        self.y_pos = -250
        self.penup()
        self.goto(self.x_pos, self.y_pos)
        self.turtlesize(1,1)
        self.setheading(90)
    
    def move_up(self):
        self.setheading(90)
        self.forward(20)

    def move_right(self):
        self.x_pos += 5
        current_y = self.ycor()
        self.goto(self.x_pos, current_y)
    
    def move_left(self):
        self.x_pos -= 5
        current_y = self.ycor()
        self.goto(self.x_pos, current_y)
    
    def reset_position(self):
        self.goto(0, -250)