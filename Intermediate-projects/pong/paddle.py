from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.shapesize(5,1)
        self.color("white")
        self.penup()
        self.setposition(x_pos, y_pos)

    def up(self):
        current_y = self.ycor()
        self.goto(self.xcor(), current_y + 20)

    def down(self):
        current_y = self.ycor()
        self.goto(self.xcor(), current_y - 20)