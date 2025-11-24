import turtle
from game import Game
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
game = Game()
data = pandas.read_csv("50_states.csv")
states = list(data["state"])
already_answered = []

game_is_on = True

while game_is_on:
    current_score = game.score
    answer_state = screen.textinput(title=f"{current_score}/50 Guess the State", prompt="What's another state's name?")
    
    # Check if user cancelled the input dialog
    if answer_state.title() == "Exit":
        rest_states = list(set(states) - set(already_answered))
        file = pandas.DataFrame(rest_states, columns=["states"])
        file.to_csv("missed_states.csv")
        
        game_is_on = False
        break
        
    is_answer_correct = game.check_answer(answer_state.title(), states)
    if is_answer_correct and answer_state.title() not in already_answered:
        already_answered.append(answer_state.title())
        input_state_data = data[data["state"] == answer_state.title()]
        x_state = int(input_state_data["x"])
        y_state = int(input_state_data["y"])
        game.add_score()
        game.display_and_move_state_text(answer_state.title(), x_state, y_state)
    
    if game.score == len(states):
        game.game_over()
        game_is_on = False

## this is the block of code you will need if you have to manually get the x,y value
# def get_mounse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mounse_click_coor)


turtle.mainloop()
