import random

SIZE_GRID = 10

def create_matrix(size):
    return [['.' for _ in range(size)] for _ in range(size)]

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(row))
    print()

def place_player_and_goal(matrix):
    player_pos = (random.randint(0, SIZE_GRID - 1), random.randint(0, SIZE_GRID - 1))
    goal_pos = (random.randint(0, SIZE_GRID - 1), random.randint(0, SIZE_GRID - 1))
    
    while goal_pos == player_pos:
        goal_pos = (random.randint(0, SIZE_GRID - 1), random.randint(0, SIZE_GRID - 1))
    
    matrix[player_pos[0]][player_pos[1]] = 'P'
    matrix[goal_pos[0]][goal_pos[1]] = 'G'
    
    return player_pos, goal_pos

def move_player(matrix, player_pos, direction):
    x, y = player_pos
    matrix[x][y] = '.'
    
    if direction == '8' and x > 0:
        x -= 1
    elif direction == '2' and x < SIZE_GRID - 1:
        x += 1
    elif direction == '4' and y > 0:
        y -= 1
    elif direction == '6' and y < SIZE_GRID - 1:
        y += 1
    
    matrix[x][y] = 'P'
    return (x, y)

def main():
    matrix = create_matrix(SIZE_GRID)
    player_pos, goal_pos = place_player_and_goal(matrix)
    steps = 0
    
    print("Welcome to the Maze Game!")
    print("Use 8 (up), 2 (down), 4 (left), 6 (right) to move.")
    print("Try to reach the goal 'G' from your position 'P'.")
    
    while True:
        print_matrix(matrix)
        move = input("Enter your move (8/2/4/6) or 'q' to quit: ")
        
        if move == 'q':
            print("Game over. You quit the game.")
            break
        
        if move in ['8', '2', '4', '6']:
            player_pos = move_player(matrix, player_pos, move)
            steps += 1
            
            if player_pos == goal_pos:
                print_matrix(matrix)
                print(f"Congratulations! You reached the goal in {steps} steps.")
                break
        else:
            print("Invalid move. Please enter 8, 2, 4, 6 or 'q'.")

if __name__ == "__main__":
    main()