import turtle  # Import the turtle module for graphical operations
import pandas as pd  # Import pandas for data manipulation

# Function to write state name and its coordinates to a text file
def write_to_text_file(state_name, x, y):
    with open("states.txt", 'a') as file:  # Open the file in append mode
        file.write(f"{state_name},{x},{y}\n")  # Write the state name and coordinates to the file

# Function to get the coordinates when the mouse is clicked
def get_mouse_click_coordinates(x, y):
    state_name = screen.textinput("State Name", "Enter the state name: ")  # Prompt the user to enter a state name
    if state_name:  # Check if a state name was entered
        write_to_text_file(state_name, x, y)  # Write the state name and coordinates to the text file

# Function to convert the text file to a CSV file
def convert_txt_to_csv():
    data = pd.read_csv("states.txt", header=None)  # Read the text file into a DataFrame
    data.columns = ["state", "x", "y"]  # Set the column names
    data.to_csv("states.csv", index=False)  # Save the DataFrame to a CSV file

# Main block to ensure the code runs only when executed directly
if __name__ == '__main__':
    screen = turtle.Screen()  # Create a screen object for the map
    screen.title("India Outline Map")  # Set the title of the window
    image = "India-outline-map.gif"  # Define the path to the map image
    screen.addshape(image)  # Add the image shape to the turtle screen
    turtle.shape(image)  # Set the turtle shape to the map image
    turtle.onscreenclick(get_mouse_click_coordinates)  # Set the function to call on mouse click
    turtle.mainloop()  # Start the turtle main loop to listen for events

    convert_txt_to_csv()  # Convert the text file to a CSV file after the main loop exits
