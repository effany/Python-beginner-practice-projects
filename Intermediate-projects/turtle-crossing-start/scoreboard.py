from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("Black")
        self.level = 1
        self.penup()
        self.goto(-230, 250)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Car Crash! Game Over!", True, align="center", font=FONT)

    
    def level_up(self):
        self.clear()
        self.level += 1
        self.goto(-230, 250)
        self.write(f"Level: {self.level}", align="center", font=FONT)