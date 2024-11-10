import numpy as np
import random
import os

SIZE_GRID = 10

def create_matrix(size):
    return np.full((size, size), '.')

def place_player_and_goal(matrix):
    player_pos = (random.randint(0, SIZE_GRID - 1), random.randint(0, SIZE_GRID - 1))
    goal_pos = (random.randint(0, SIZE_GRID - 1), random.randint(0, SIZE_GRID - 1))
    while goal_pos == player_pos:
        goal_pos = (random.randint(0, SIZE_GRID - 1), random.randint(0, SIZE_GRID - 1))
    return player_pos, goal_pos

def print_matrix(matrix, player_pos, goal_pos):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
    temp_matrix = matrix.copy()
    temp_matrix[player_pos] = 'P'
    temp_matrix[goal_pos] = 'G'
    for row in temp_matrix:
        print(' '.join(row))
    print()

def move_player(player_pos, direction):
    x, y = player_pos
    if direction == '8' and x > 0:
        x -= 1
    elif direction == '2' and x < SIZE_GRID - 1:
        x += 1
    elif direction == '4' and y > 0:
        y -= 1
    elif direction == '6' and y < SIZE_GRID - 1:
        y += 1
    return (x, y)

def main():
    matrix = create_matrix(SIZE_GRID)
    player_pos, goal_pos = place_player_and_goal(matrix)
    steps = 0

    print("Welcome to the Maze Game!")
    print("Use the following keys to move:")
    print("8 - Up, 2 - Down, 4 - Left, 6 - Right")
    print("Reach the goal 'G' to win!\n")

    while True:
        print_matrix(matrix, player_pos, goal_pos)
        move = input("Enter your move (8/2/4/6) or 'q' to quit: ")
        if move == 'q':
            print("Game over. You quit the game.")
            break
        if move in ['8', '2', '4', '6']:
            player_pos = move_player(player_pos, move)
            steps += 1
            if player_pos == goal_pos:
                print_matrix(matrix, player_pos, goal_pos)
                print(f"Congratulations! You reached the goal in {steps} steps.")
                break
        else:
            print("Invalid input. Please enter 8, 2, 4, 6 or 'q'.")

if __name__ == "__main__":
    main()