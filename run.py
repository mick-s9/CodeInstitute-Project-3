
# python code goes here
import random
import math

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
def get_user_guess(size):
    while True:
        try:
            guessRow = int(input("Enter your guess row: \n"))
            guessColumn = int(input("Enter your guess column: \n"))
            if 0 <= guessRow < size and 0 <= guessColumn < size:
                return guessRow, guessColumn
            else:
                print("Your guess is off-grid. Try again.")
        except ValueError:
            print("Invalid input. Please enter two numeric characters.")

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
    

# Main function to play the game
def play_battleships():
    print("Welcome to Battleships!")
    while True:
        size = 0
        num_ships = 0

        while size <= 1:
            size = int(input("Enter the grid size (must be greater than 1): \n"))
            if size <= 1:
                print("Please enter a number greater than 1.")

        while num_ships <= 0:
            num_ships = int(input("Enter the number of battleships (must be greater than 0): \n"))
            if num_ships <= 0:
                print("Please enter a number greater than 0.")

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
            user_x, user_y = get_user_guess(size)
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

        play_again = input("Do you want to play again? (yes/no):\n")
        if play_again.lower() != 'yes':
            print("Thank you for playing. Goodbye!")
            break

# Run the game
if __name__ == "__main__":
    play_battleships()