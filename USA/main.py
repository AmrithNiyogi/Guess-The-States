import turtle  # Import the turtle module for graphical operations
import pandas as pd  # Import pandas for data manipulation

# The main block to ensure the code runs only when executed directly
if __name__ == '__main__':
    screen = turtle.Screen()  # Create a screen object for the game
    screen.title("U.S. States Game")  # Set the title of the window
    image = "blank_states_img.gif"  # Define the path to the background image
    screen.addshape(image)  # Add the image shape to the turtle screen
    turtle.shape(image)  # Set the turtle shape to the background image

    data = pd.read_csv("50_states.csv")  # Read the states data from the CSV file
    all_states = data.state.to_list()  # Convert the state names to a list
    guessed_states = []  # Initialize an empty list to keep track of guessed states

    # Continue the game until all 50 states are guessed
    while len(guessed_states) < 50:
        # Prompt the user to enter a state name
        answer_state = screen.textinput(title=f"{len(guessed_states)/50} States Correct",
                                        prompt="What's another state's name").title()

        # If the user types "Exit", break out of the loop and save missing states to a CSV file
        if answer_state == "Exit":
            missing_states = []  # Initialize an empty list for missing states
            for state in all_states:  # Loop through all states
                if state not in guessed_states:  # Check if the state has not been guessed
                    missing_states.append(state)  # Add the state to the missing states list
            new_data = pd.DataFrame(missing_states)  # Create a DataFrame from the missing states list
            new_data.columns = ["State"]  # Rename the column to "State"
            new_data.to_csv("states_to_learn.csv")  # Save the DataFrame to a CSV file
            break  # Exit the loop

        # If the entered state is correct and in the list of all states
        if answer_state in all_states:
            guessed_states.append(answer_state)  # Add the guessed state to the list
            t = turtle.Turtle()  # Create a new turtle object
            t.hideturtle()  # Hide the turtle icon
            t.penup()  # Lift the pen to avoid drawing lines
            state_data = data[data.state == answer_state]  # Get the data for the guessed state
            t.goto(int(state_data.x), int(state_data.y))  # Move the turtle to the state's coordinates
            t.write(state_data.state.item())  # Write the state name at the specified location
