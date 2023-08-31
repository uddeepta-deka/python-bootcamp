import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
place = turtle.Turtle()
place.penup()
place.hideturtle()

states_data = pandas.read_csv("50_states.csv")
all_states = states_data["state"].to_list()


score = 0
lives = 4
guessed_states = []
while score < 50 and lives > 0:
    answer_state = screen.textinput(title=f"{score}/50 states guessed.", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        print(f"Your final score is {score}")
        break
    if answer_state in guessed_states:
        print(f"{answer_state} already guessed! Try some other state.")
    elif answer_state in all_states and answer_state not in guessed_states:
        data = states_data[states_data.state == answer_state]
        place.goto(int(data.x), int(data.y))
        place.write(answer_state)
        score += 1
        guessed_states.append(answer_state)
        if score == 50:
            print("Congratulations!! You've guessed all the states of the U.S.A.")
    else:
        lives -= 1
        if lives > 0:
            print(f"{answer_state} is not a state of the U.S.A. You have {lives} lives left.")
        else:
            print(f"You are out of lives. Your final score is: {score}")

# saving the missing states to a txt file
states_missed = [state for state in all_states if state not in guessed_states]
df = pandas.DataFrame(states_missed)
df.to_csv("states_to_learn.csv")

screen.exitonclick()