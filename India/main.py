import turtle
import pandas as pd

if __name__ == '__main__':
    screen = turtle.Screen()
    screen.title("India States Game")
    image = "India-outline-map.gif"
    screen.addshape(image)
    turtle.shape(image)

    data = pd.read_csv("states.csv")
    all_states = data.state.to_list()
    guessed_states = []
    while len(guessed_states) < 50:
        answer_state = screen.textinput(title=f"{len(guessed_states)/33} States Correct",
                                        prompt="What's another state's name").title()

        if answer_state == "Exit":
            missing_states = []
            for state in all_states:
                if state not in guessed_states:
                    missing_states.append(state)
            new_data = pd.DataFrame(missing_states)
            new_data.columns("State")
            new_data.to_csv("states_to_learn.csv")
            break

        if answer_state in all_states:
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(state_data.state.item())
