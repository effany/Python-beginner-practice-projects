import pandas
from turtle import Turtle

class Game(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
    
    def check_answer(self, user_input, state_list):
        print(user_input, state_list)
        return True if user_input in state_list else False
    
    def add_score(self):
        self.score += 1
    
    def display_and_move_state_text(self, state, x, y):
        self.penup()
        self.goto(x, y)
        self.write(state, align="center", font=("Courier", 12, "normal"))
    
    def game_over(self):
        self.goto(0,0)
        self.hideturtle()
        self.write("Congratulations!", align="center", font=("Courier", 70, "bold"))
        
    
        


    


    
    

