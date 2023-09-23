import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.tolist()

game_active = True
correct_guesses = []


def write_state(x_cor, y_cor, state):
    state_name = turtle.Turtle()
    state_name.hideturtle()
    state_name.penup()
    state_name.setpos(x_cor, y_cor)
    state_name.write(f"{state}", align="center", font=("Courier", 10, "normal"))


while game_active:
    score = len(correct_guesses)
    answer = screen.textinput(f"{score}/50 States Correct", "Enter a state:").title()
    if answer == "Exit":
        break
    elif answer in states:
        correct_guesses.append(answer)
        row = data[data.state == answer]
        row_list = row.to_dict()
        row_num = 0
        for key, value in row_list["state"].items():
            row_num = key
        x = row_list["x"][row_num]
        y = row_list["y"][row_num]
        write_state(x, y, answer)
        print("correct!")
    else:
        print("dummy!")
    if score == 50:
        game_active = False

missed_answers = []
for state in states:
    if state not in correct_guesses:
        missed_answers.append(state)

state_dict = {
    "states": missed_answers
}

df = pandas.DataFrame(state_dict)
df.to_csv("States_to_Learn.csv")