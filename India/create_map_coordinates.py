import turtle
import pandas as pd


def write_to_text_file(state_name, x, y):
    with open("states.txt", 'a') as file:
        file.write(f"{state_name},{x},{y}\n")


def get_mouse_click_coordinates(x, y):
    state_name = screen.textinput("State Name", "Enter the state name: ")
    if state_name:
        write_to_text_file(state_name, x, y)


def convert_txt_to_csv():
    data = pd.read_csv("states.txt", header=None)
    data.columns = ["state", "x", "y"]
    data.to_csv("states.csv", index=False)


if __name__ == '__main__':
    screen = turtle.Screen()
    screen.title("India Outline Map")
    image = "India-outline-map.gif"
    screen.addshape(image)
    turtle.shape(image)
    turtle.onscreenclick(get_mouse_click_coordinates)
    turtle.mainloop()

    convert_txt_to_csv()
