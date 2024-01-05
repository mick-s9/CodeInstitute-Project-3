
# -*- coding: utf-8 -*-

import random
import math

try:
    from flask import Flask, request
    print("Flask è installato correttamente.")
    app = Flask(__name__)
except ImportError:
    print("Errore: Flask non è installato.")



# Function to create a grid of given size
def create_grid(size):
    return [['0' for _ in range(size)] for _ in range(size)]

# Function to print the grid
def print_grid(grid):
    for row in grid:
        print(" ".join(row))

# Function to place battleships randomly on the grid
def place_battleships(grid, num_ships):
    size = len(grid)
    for _ in range(num_ships):
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        while grid[x][y] == 'X':
            x = random.randint(0, size - 1)
            y = random.randint(0, size - 1)
        grid[x][y] = 'X'

# Function to calculate distance to the nearest battleship
def calculate_distance(grid, x, y):
    size = len(grid)
    min_distance = size  # Maximum possible distance
    for i in range(size):
        for j in range(size):
            if grid[i][j] == 'X':
                distance = math.sqrt((x - i)**2 + (y - j)**2)
                min_distance = min(min_distance, distance)
    return round(min_distance, 2)

# Function to get user's guess and validate if it's on the grid
def get_user_guess_from_request(request_data):
    try:
        guessRow = int(request_data.get('guessRow'))
        guessColumn = int(request_data.get('guessColumn'))
        return guessRow, guessColumn
    except (ValueError, TypeError):
        return None

# Function for computer's guess
def get_computer_guess(size):
    x = random.randint(0, size - 1)
    y = random.randint(0, size - 1)
    return x, y

def count_total_sunk(grid):
    return sum(row.count('*') for row in grid)

# function to copy the striked ships to the computer (hide) grid
def copy_stars(source_grid, destination_grid):
    for row in range(len(source_grid)):
        for col in range(len(source_grid[row])):
            if source_grid[row][col] == '*':
                destination_grid[row][col] = '*'

# Flask route to handle game requests
@app.route('/play', methods=['POST'])
def play():
    data = request.form.to_dict()

    size = int(data.get('size', 0))
    num_ships = int(data.get('num_ships', 0))

    user_grid = create_grid(size)
    computer_grid = create_grid(size)
    computer_grid_hide = create_grid(size)

    place_battleships(user_grid, num_ships)
    place_battleships(computer_grid, num_ships)

    user_attempts = 0
    computer_attempts = 0

    while True:
        print("Your Grid:")
        print_grid(user_grid)

        copy_stars(computer_grid, computer_grid_hide)

        print("Computer's Grid:")
        print_grid(computer_grid_hide)

        # User's turn
        print("Your Turn:")
        user_guess = get_user_guess_from_request(data)
        if user_guess is not None:
            user_x, user_y = user_guess
            if computer_grid[user_x][user_y] == 'X':
                print("Congratulations! You hit a battleship!")
                computer_grid[user_x][user_y] = '*'
                user_attempts += 1
            else:
                print("Oops! You missed.")
                user_attempts += 1

        # Computer's turn
        print("Computer's Turn:")
        comp_x, comp_y = get_computer_guess(size)
        if user_grid[comp_x][comp_y] == 'X':
            print("Computer hit your battleship!")
            user_grid[comp_x][comp_y] = '*'
            computer_attempts += 1
        else:
            print("Computer missed.")
            computer_attempts += 1

        # Check game end conditions
        if count_total_sunk(computer_grid) == num_ships:
            print("Congratulations! You sank all the computer's battleships in", user_attempts, "attempts.")
            break

        if all('X' not in row for row in user_grid):
            print("Computer sank all your battleships in", computer_attempts, "attempts. Better luck next time!")
            break

    return "Game over"

if __name__ == "__main__":
    app.run(port=5000)  # Run the Flask app locally on port 5000

