# State Guessing Games

This project contains two interactive games to help users learn the states of the United States and India. 

## Table of Contents

-[Overview](#overview)
  -[Project Structure](#project-structure)
-[Features](#features)
-[Installation](#installation)
-[Usage](#usage)
-[How to Play and Controls](#how-to-play-and-controls)
-[Code Structure](#code-structure)
-[Contributing](#contributing)
-[License](#license)

## Overview

Each game presents an outline map of the respective country, and users must guess the states by entering their names. If a state is guessed correctly, it is displayed on the map at its corresponding location.

### Project Structure

The project has two main directories:
- `US States Game`
- `India States Game`

## Features

### US States Game
- **Interactive Map**: Displays an outline map of the United States.
- **State Guessing**: Users can input state names to guess their locations.
- **Real-time Feedback**: Correctly guessed states are displayed on the map at their respective coordinates.
- **Exit Option**: Users can type "Exit" to stop the game at any time.
- **Learning Mode**: On exit, a CSV file (`states_to_learn.csv`) is generated, listing the states that were not guessed correctly.

### India States Game
- **Interactive Map**: Displays an outline map of India.
- **State Guessing**: Users can input state names to guess their locations.
- **Real-time Feedback**: Correctly guessed states are displayed on the map at their respective coordinates.
- **Exit Option**: Users can type "Exit" to stop the game at any time.
- **Learning Mode**: On exit, a CSV file (`states_to_learn.csv`) is generated, listing the states that were not guessed correctly.
- **Coordinate Creation Tool**: Includes a script (`create_map_coordinates.py`) that allows users to click on the map to record state coordinates, which are then converted into a CSV file (`states.csv`).


## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/AmrithNiyogi/guess-the-states.git
    ```

2. Navigate to the project directory:
    ```sh
    cd India
    ```
    or
   ```sh
   cd USA
   ```

4. Ensure you have Python installed (preferably version 3.6 or above).

5. Install the required dependencies (if any)

## Usage

##### You can use the India directory as a template and create games for different countries.

To start the game, go the respective directory of the game you want to play, run the following command:
```sh
python main.py
```

## How to Play and Controls

### How to Play

#### US States Game

1. Navigate to the `US States Game` directory.
2. Run the `us_states_game.py` script.
3. A map of the United States will be displayed. Enter the names of the states to mark them on the map.
4. If you wish to exit before completing, type "Exit". A CSV file `states_to_learn.csv` will be created with the states you missed.

#### India States Game

##### Running the Game

1. Navigate to the `India States Game` directory.
2. Run the `main.py` script.
3. A map of India will be displayed. Enter the names of the states to mark them on the map.
4. If you wish to exit before completing, type "Exit". A CSV file `states_to_learn.csv` will be created with the states you missed.

##### Creating the `states.csv` File

If `states.csv` is not available or needs to be updated:
1. Run the `create_map_coordinates.py` script.
2. Click on the map to mark the coordinates of each state. You will be prompted to enter the state's name.
3. After entering all states, close the window. The coordinates will be saved in `states.txt`.
4. The script will automatically convert `states.txt` to `states.csv`.


### Controls

- Enter a state as a guess and see how far you can go.
- Enter the word `Exit` to end the game.
Enjoy learning the states!

## Code Structures

### US States Game

This directory contains:
- `50_states.csv`: A CSV file with the list of U.S. states and their coordinates.
- `blank_states_img.gif`: An image of the U.S. map.
- `us_states_game.py`: The main code for the U.S. States Game.

### India States Game

This directory contains:
-`states.csv`: A CSV file with the list of Indian states and their coordinates.
- `states.txt`: A text file used for creating the CSV file of Indian states and their coordinates.
- `India-outline-map.gif`: An image of the India map.
- `main.py`: The main code for the India States Game.
- `create_map_coordinates.py`: A helper script to create `states.csv` from mouse clicks on the map.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
